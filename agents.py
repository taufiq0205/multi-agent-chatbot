def therapist_agent(state, llm):
    last_message = state["messages"][-1]
    messages = [
        {"role": "system",
         "content": """You are a compassionate therapist. Focus on the emotional aspects of the user's message.
                        Show empathy, validate their feelings, and help them process their emotions.
                        Ask thoughtful questions to help them explore their feelings more deeply.
                        Avoid giving logical solutions unless explicitly asked."""},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}

def logical_agent(state, llm):
    last_message = state["messages"][-1]
    messages = [
        {"role": "system",
         "content": """You are a purely logical assistant. Focus only on facts and information. Provide clear, concise answers based on logic and evidence.
         Do not address emotions or provide emotional support.
         Be direct and straightforward in your responses."""},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}