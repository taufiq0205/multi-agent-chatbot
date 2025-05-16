from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from graph_builder import build_graph

load_dotenv()
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
graph = build_graph(llm)

try:
    ascii_art = graph.get_graph().print_ascii()
    print(ascii_art)
except Exception as e:
    print(f"An error occurred: {e}")