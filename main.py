from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()
tools = [TavilySearch()]



llm = ChatOpenAI()

agent = create_agent(
    model=llm,
    tools=tools,
)

def main():
    print("Hello from langchain-course-1!")
    result = agent.invoke(
        {"messages": [HumanMessage(content="What is weather in Tokyo?")]},
    )
    print(f"Agent result: {result}")

if __name__ == "__main__":
    main()





