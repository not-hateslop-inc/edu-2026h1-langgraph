from dotenv import load_dotenv
from langchain.agents import create_agent
from tools import TOOLS

load_dotenv()
agent = create_agent("openai:gpt-4o-mini", tools=TOOLS, system_prompt="헤이트슬롭 회의실 도우미다.")
r = agent.invoke({"messages": [("user", "다음 주 월요일(2026-04-27) 8명 회의실 잡아줘")]})
for m in r["messages"]:
    print(type(m).__name__, getattr(m, "tool_calls", None) or m.content)
