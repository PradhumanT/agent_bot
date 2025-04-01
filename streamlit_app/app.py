import streamlit as st
from dotenv import load_dotenv
import tempfile

from agent_backend.llm import load_llm
from agent_backend.memory import get_memory
from agent_backend.tools import load_basic_tools
from agent_backend.agent import build_agent
from agent_backend.rag import create_pinecone_retriever_from_pdf
from langchain.agents import Tool

load_dotenv()

st.set_page_config(page_title="🤖 Smart PDF Chatbot", layout="wide")
st.title("🧠 Intelligent Agent Chatbot with Tools + Optional PDF")

# Initialize session state
if "llm" not in st.session_state:
    st.session_state.llm = load_llm()
if "memory" not in st.session_state:
    st.session_state.memory = get_memory()
if "tools" not in st.session_state:
    st.session_state.tools = load_basic_tools()
if "agent" not in st.session_state:
    st.session_state.agent = build_agent(
        llm=st.session_state.llm,
        tools=st.session_state.tools,
        memory=st.session_state.memory
    )
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "rag_loaded" not in st.session_state:
    st.session_state.rag_loaded = False

# PDF Upload (optional)
uploaded_file = st.file_uploader("📄 Optionally upload a PDF file", type=["pdf"])
if uploaded_file and not st.session_state.rag_loaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    retriever, namespace = create_pinecone_retriever_from_pdf(pdf_path)

    rag_tool = Tool(
        name="Document_Retrieval",
        func=lambda q: retriever.get_relevant_documents(q),
        description="Use this if the user has uploaded a document and asks about its contents."
    )

    st.session_state.tools.append(rag_tool)
    st.session_state.agent = build_agent(
        llm=st.session_state.llm,
        tools=st.session_state.tools,
        memory=st.session_state.memory
    )
    st.session_state.rag_loaded = True
    st.success("✅ Document uploaded. You can now ask about it.")

# Chat input + response
user_input = st.chat_input("Ask me anything...")
if user_input:
    with st.spinner("Thinking..."):
        try:
            response = st.session_state.agent.invoke(user_input)
            bot_msg = response["output"] if isinstance(response, dict) else response
        except Exception as e:
            bot_msg = f"⚠️ Error: {str(e)}"

    st.session_state.chat_history.append((user_input, bot_msg))

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    st.chat_message("user").markdown(user_msg)
    st.chat_message("assistant").markdown(bot_msg)
