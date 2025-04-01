import streamlit as st
from agent_backend.llm import load_llm
from agent_backend.memory import get_memory
from agent_backend.tools import load_basic_tools
from agent_backend.rag import create_pinecone_retriever_from_pdf
from agent_backend.agent import build_agent
import tempfile

st.set_page_config(page_title="📚 Smart PDF Chatbot", layout="wide")
st.title("🤖 Intelligent Agent Chatbot with RAG + Tools")

# Session state for agent + chat history
if "agent" not in st.session_state:
    st.session_state.agent = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# File upload
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])
if uploaded_file is not None and st.session_state.agent is None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Build components
    llm = load_llm()
    memory = get_memory()
    tools = load_basic_tools()

    retriever, namespace = create_pinecone_retriever_from_pdf(pdf_path)
    from langchain.agents import Tool
    rag_tool = Tool(
        name="Document_Retrieval",
        func=lambda q: retriever.get_relevant_documents(q),
        description="Use this to answer questions about the uploaded document."
    )
    tools.append(rag_tool)

    # Build agent
    st.session_state.agent = build_agent(llm, tools, memory)
    st.success("✅ Agent initialized!")

# Chat input
if st.session_state.agent:
    user_input = st.chat_input("Ask a question about the document or anything else...")
    if user_input:
        with st.spinner("Thinking..."):
            response = st.session_state.agent.invoke(user_input)
            st.session_state.chat_history.append((user_input, response["output"] if isinstance(response, dict) else response))

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    st.chat_message("user").markdown(user_msg)
    st.chat_message("assistant").markdown(bot_msg)
