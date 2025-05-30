# LangGraph Tutorial

This project demonstrates a multi-agent chatbot using [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain). The chatbot routes user messages to a family of specialized conversational agents—including "therapist", "logical", "motivational", "humor", and "greeting" agents—based on message classification.

## Features

- **Message Classification:** Automatically classifies user messages as requiring emotional support, logical reasoning, motivation, humor, or greeting/farewell.
- **Specialized Agents:**
  - **Therapist Agent:** Provides empathetic, emotionally supportive responses.
  - **Logical Agent:** Provides direct, fact-based answers.
  - **Motivational Agent:** Offers encouragement and motivation.
  - **Humor Agent:** Responds with jokes or light-hearted comments.
  - **Greeting Agent:** Handles greetings and farewells.
- **Graph-based Routing:** Uses a state graph to manage the flow between classification and agent response.
- **Visualization:** Generates a diagram of the agent routing graph.

## Project Structure

- `main.py` — Entry point for running the chatbot in the terminal.
- `agents.py` — Contains the implementations for all specialized agents.
- `graph_builder.py` — Builds the LangGraph state graph and routing logic.
- `state.py` — Defines the state and message classification schema.
- `visualize_graph.py` — Script to generate a visualization of the agent routing graph.
- `.env` — Store your API keys and environment variables here.
- `pyproject.toml` — Project dependencies and metadata.

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/taufiq0205/multi-agent-chatbot.git
    cd langgraph-tutorial
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    Or, if using Poetry or another tool, install as appropriate.

3. **Set up environment variables:**
    - Create a `.env` file with your API keys (see `.env` example).

4. **Run the chatbot:**
    ```bash
    python main.py
    ```

5. **Visualize the graph (optional):**
    ```bash
    python visualize_graph.py
    ```

## Requirements

- Python 3.12+
- See `pyproject.toml` for required packages.

## Example Usage
```bash
Message: I feel sad and overwhelmed.
Assistant: I'm sorry you're feeling this way. Can you tell me more about what's been making you feel overwhelmed?

Message: Why did the chicken cross the road?
Assistant: To get to the other side! (humor agent)

Message: Hello!
Assistant: Hi there! How can I assist you today? (greeting agent)
```

*This project is for educational purposes and demonstrates multi-agent orchestration with LangGraph and LangChain.*
