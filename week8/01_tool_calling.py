from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tools import TOOLS

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini").bind_tools(TOOLS)
msg = llm.invoke("8명이 회의할 방 찾아줘")
print(msg.tool_calls)
