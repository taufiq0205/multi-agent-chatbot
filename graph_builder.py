from langgraph.graph import StateGraph, START, END
from state import State, MessageClassifier
from agents import therapist_agent, logical_agent

def classify_message(state, llm):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {"role": "system", "content": "..."},
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}

def router(state):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}
    return {"next": "logical"}

def build_graph(llm):
    graph_builder = StateGraph(State)
    graph_builder.add_node("classifier", lambda state: classify_message(state, llm))
    graph_builder.add_node("router", router)
    graph_builder.add_node("therapist", lambda state: therapist_agent(state, llm))
    graph_builder.add_node("logical", lambda state: logical_agent(state, llm))
    graph_builder.add_edge(START, "classifier")
    graph_builder.add_edge("classifier", "router")
    graph_builder.add_conditional_edges(
        "router",
        lambda state: state.get("next"),
        {"therapist": "therapist", "logical": "logical"}
    )
    graph_builder.add_edge("therapist", END)
    graph_builder.add_edge("logical", END)
    return graph_builder.compile()