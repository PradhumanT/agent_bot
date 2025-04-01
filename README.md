# 🤖 Intelligent LangChain Chatbot with Tools, RAG, and Streamlit

A modular, production-ready chatbot built using [LangChain](https://www.langchain.com/), [Gemini Flash (via Google GenAI)](https://ai.google.dev/), [Pinecone](https://www.pinecone.io/), and [Streamlit](https://streamlit.io/). The chatbot behaves like a smart agent with tools and memory — and supports optional document upload for Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 🧠 **LLM**: Gemini Flash model via `langchain-google-genai`
- 💡 **Tools**:
  - Python REPL (for code/math)
  - Wikipedia search
  - Web search via SERP API
  - PDF-based RAG using Pinecone (optional upload)
- 🔄 **Memory**: Conversation context retained across turns
- 📄 **Optional PDF Upload**: Users can upload a document anytime
- 🗂️ **Modular Backend** with clean architecture (`agent_backend/`)
- 🖥️ **Streamlit UI** with real-time chat interface

---

## 🧱 Project Structure

```
agent-chatbot/
├── agent_backend/
│   ├── __init__.py
│   ├── llm.py            # Gemini Flash LLM setup
│   ├── tools.py          # Wikipedia, Python REPL, SERP API tools
│   ├── rag.py            # PDF upload → embedding → Pinecone
│   ├── memory.py         # ConversationBufferMemory
│   └── agent.py          # Assembles the LangChain agent
├── streamlit_app/
│   └── app.py            # Frontend UI using Streamlit
├── .env                  # API keys and config
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/agent-chatbot.git
cd agent-chatbot
```

### 2. Create and Activate Conda Environment

```bash
conda create -n agent_bot python=3.10
conda activate agent_bot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root:

```
GOOGLE_API_KEY=your_gemini_flash_api_key
SERPAPI_API_KEY=your_serpapi_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_pinecone_environment
```

---

## 🧪 Run Locally

```bash
streamlit run streamlit_app/app.py
```

- Chatbot will start with basic tools (code, wiki, web)
- You can upload a PDF anytime during the session
- After upload, the bot can answer questions about the document

---

## ☁️ Deployment

You can deploy this on AWS EC2 (free-tier friendly) with:

- `tmux` or `pm2` for persistence
- Nginx or port tunneling (if needed)
- Copy your `.env` securely via `scp` or `.pem`

📝 [Deployment guide coming soon...]

---

## 🛡️ TODO / Roadmap

- [ ] Streaming responses in chat
- [ ] PDF multi-file support
- [ ] User-specific history & namespaces
- [ ] Auth & session management
- [ ] Export chat history

---

## 📜 License

MIT License. Free to use, modify, and build on!

---

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Google GenAI](https://ai.google.dev/)
- [Pinecone Vector DB](https://www.pinecone.io/)
- [Streamlit](https://streamlit.io/)
