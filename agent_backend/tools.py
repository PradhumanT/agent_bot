from langchain.agents import Tool
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.utilities import SerpAPIWrapper
import os

def load_basic_tools():
    wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    python_tool = PythonREPLTool()
    serp = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

    return [
        Tool(name="Python_REPL", func=python_tool.run,
             description="Useful for executing Python code for tasks such as math, logic, and plotting."),
        Tool(name="Wikipedia", func=wiki.run,
             description="Useful for retrieving factual and historical information from Wikipedia."),
        Tool(name="Web_Search", func=serp.run,
             description="Useful for answering current event or factual queries using the SERP API.")
    ]
