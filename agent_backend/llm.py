from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()


def load_llm(temperature=0.2):
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        convert_system_message_to_human=True,
        temperature=temperature
    )
