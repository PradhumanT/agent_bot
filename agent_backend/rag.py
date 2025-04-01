from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
import uuid
import os

def create_pinecone_retriever_from_pdf(pdf_path, index_name="doc-chatbot"):
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    namespace = f"session-{uuid.uuid4()}"

    vectorstore = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embed_model,
        index_name=index_name,
        namespace=namespace
    )

    return vectorstore.as_retriever(), namespace
