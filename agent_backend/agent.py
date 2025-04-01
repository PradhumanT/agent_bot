from langchain.agents import initialize_agent

def build_agent(llm, tools, memory):
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="conversational-react-description",
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
