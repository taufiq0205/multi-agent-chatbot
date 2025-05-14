from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from graph_builder import build_graph

load_dotenv()
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
graph = build_graph(llm)

try:
    image_data = graph.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(image_data)
    print("Graph saved as graph.png")
except Exception as e:
    print(f"An error occurred: {e}")