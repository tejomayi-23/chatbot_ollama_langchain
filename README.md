# Simple Chatbot with Ollama, LangChain & Streamlit

A simple chatbot web app that runs a large language model **locally** on your machine. It uses [Ollama](https://ollama.com/) to serve the model, [LangChain](https://www.langchain.com/) to talk to it, and [Streamlit](https://streamlit.io/) for the user interface. No API key or internet connection is needed once the model is downloaded.

## Features

- Clean web interface built with Streamlit
- Runs entirely locally using the `llama3.2:3b` model (no API costs)
- Text box to enter questions, with a loading spinner while the response is generated
- Chat history displayed on the page, with the newest messages first
- Session-based history that lasts until the browser tab is refreshed or closed

## Tech Stack

| Component | Purpose |
|-----------|---------|
| Python 3.9+ | Programming language |
| Streamlit | Web UI |
| LangChain (`langchain-ollama`) | Interface between the app and the model |
| Ollama | Local LLM runtime |
| Llama 3.2 (3B) | Language model |

## Project Structure

```
.
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
```

## Prerequisites

- Python 3.9 or higher
- [Ollama](https://ollama.com/download) installed on your system
- About 4 GB of free RAM and about 2 GB of disk space for the model

## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Install Ollama

Download and install it from [https://ollama.com/download](https://ollama.com/download), then verify the installation:

```bash
ollama --version
```

### 3. Download the model

```bash
ollama pull llama3.2:3b
```

### 4. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 5. Install the Python dependencies

```bash
pip install streamlit langchain langchain-ollama
```

## How to Run

1. Make sure Ollama is running. It usually starts automatically after installation. If not, start it with:

```bash
   ollama serve
```

2. Start the Streamlit app:

```bash
   streamlit run app.py
```

3. Open your browser at **http://localhost:8501** if it doesn't open automatically.

## Usage

1. Type your question in the text box.
2. Click **submit**.
3. Wait a few seconds for the response to appear.
4. Scroll down to see the full chat history.

## How It Works

1. The user enters a question in the Streamlit form.
2. `generate_response()` creates a `ChatOllama` instance for `llama3.2:3b` and calls `model.invoke()` with the text.
3. The response is displayed and saved in `st.session_state["chat_history"]`.
4. The history is displayed in reverse order so the latest chat appears first.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `Connection refused` / cannot connect to Ollama | Make sure Ollama is running (`ollama serve`) |
| `model "llama3.2:3b" not found` | Run `ollama pull llama3.2:3b` |
| `ModuleNotFoundError` | Activate your virtual environment and reinstall the dependencies |
| Slow responses | Close other heavy applications, or use a smaller model |

## Limitations

- The bot has **no conversational memory**. Each question is sent independently, so it can't refer back to earlier messages.
- Chat history is lost when the page is refreshed.
- Responses appear all at once rather than streaming word by word.

## Future Improvements

- Add conversation memory so the model remembers earlier messages
- Stream responses token by token
- Add a model selector in the sidebar
- Save chat history to a file or database
- Add a "Clear chat" button

## Acknowledgements

Based on the tutorial: [https://www.youtube.com/watch?v=vJOGC8QJZJQ](https://www.youtube.com/watch?v=vJOGC8QJZJQ)

## License

This project is open source and available under the [MIT License](LICENSE).