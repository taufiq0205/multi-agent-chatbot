from langgraph.graph import StateGraph, START, END
from state import State, MessageClassifier
from agents import therapist_agent, logical_agent, motivational_agent, humor_agent, greeting_agent

def classify_message(state, llm):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {"role": "system", "content": """You are a message classifier. Classify the user's message as one of:
- emotional: Needs empathy or emotional support.
- logical: Needs facts, information, or logical reasoning.
- motivational: Needs encouragement or motivation.
- humor: Is a joke or meant to be funny.
- greeting: Is a greeting or farewell.

Examples:
"I feel sad." -> emotional
"How do I fix my computer?" -> logical
"I can do this, right?" -> motivational
"Why did the chicken cross the road?" -> humor
"Hello!" -> greeting
"""},
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}

def router(state):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}
    if message_type == "motivational":
        return {"next": "motivational"}
    if message_type == "humor":
        return {"next": "humor"}
    if message_type == "greeting":
        return {"next": "greeting"}
    return {"next": "logical"}

def build_graph(llm):
    graph_builder = StateGraph(State)
    graph_builder.add_node("classifier", lambda state: classify_message(state, llm))
    graph_builder.add_node("router", router)
    graph_builder.add_node("therapist", lambda state: therapist_agent(state, llm))
    graph_builder.add_node("logical", lambda state: logical_agent(state, llm))
    graph_builder.add_node("motivational", lambda state: motivational_agent(state, llm))
    graph_builder.add_node("humor", lambda state: humor_agent(state, llm))
    graph_builder.add_node("greeting", lambda state: greeting_agent(state, llm))
    graph_builder.add_edge(START, "classifier")
    graph_builder.add_edge("classifier", "router")
    graph_builder.add_conditional_edges(
        "router",
        lambda state: state.get("next"),
        {
            "therapist": "therapist",
            "logical": "logical",
            "motivational": "motivational",
            "humor": "humor",
            "greeting": "greeting"
        }
    )
    graph_builder.add_edge("therapist", END)
    graph_builder.add_edge("logical", END)
    graph_builder.add_edge("motivational", END)
    graph_builder.add_edge("humor", END)
    graph_builder.add_edge("greeting", END)
    return graph_builder.compile()