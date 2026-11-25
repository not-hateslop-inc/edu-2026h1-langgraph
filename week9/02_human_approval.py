from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

load_dotenv()

@tool
def book_room(room: str, date: str) -> str:
    """회의실을 예약한다. 예약 전에 사람 승인을 받는다."""
    ok = interrupt({"action": "book_room", "room": room, "date": date})
    return "예약 완료" if ok == "yes" else "사용자가 취소함"

agent = create_agent("openai:gpt-4o-mini", tools=[book_room], checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "approve-1"}}
r = agent.invoke({"messages": [("user", "2026-05-01 A 회의실 예약해줘")]}, cfg)
print("승인 요청:", r.get("__interrupt__"))
r = agent.invoke(Command(resume=input("승인? (yes/no) ")), cfg)
print(r["messages"][-1].content)
