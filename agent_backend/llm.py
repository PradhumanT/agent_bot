from langchain_google_genai import ChatGoogleGenerativeAI
import os

def load_llm(temperature=0.2):
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        convert_system_message_to_human=True,
        temperature=temperature
    )
