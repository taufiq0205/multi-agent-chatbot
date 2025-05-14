from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from graph_builder import build_graph

load_dotenv()
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
graph = build_graph(llm)

def run_chatbot():
    state = {"messages": [], "message_type": None}
    while True:
        try:
            user_input = input("Message: ").strip()
            if user_input.lower() in {"exit", "quit", "bye"}:
                print("Goodbye")
                break
            if not user_input:
                print("Please enter a message.")
                continue
            state["messages"] = state.get("messages", []) + [
                {"role": "user", "content": user_input}
            ]
            state = graph.invoke(state)
            if state.get("messages") and len(state["messages"]) > 0:
                last_message = state["messages"][-1]
                print(f"Assistant: {last_message.content}")
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_chatbot()