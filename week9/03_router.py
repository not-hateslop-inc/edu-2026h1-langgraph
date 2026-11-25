from typing import Literal
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START, END

load_dotenv()
llm = init_chat_model("openai:gpt-4o-mini")

def route(state: MessagesState) -> Literal["policy", "general"]:
    q = state["messages"][-1].content
    label = llm.invoke(f"이 질문이 사내 규정 질문이면 policy, 아니면 general 한 단어로: {q}").content.strip()
    return "policy" if "policy" in label else "general"

def policy(state):  return {"messages": [("ai", "규정 검색 노드로 보냅니다 (week7 RAG 연결 자리)")]}
def general(state): return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("policy", policy); g.add_node("general", general)
g.add_conditional_edges(START, route)
g.add_edge("policy", END); g.add_edge("general", END)
graph = g.compile()
for q in ["연차 며칠이야?", "점심 메뉴 추천해줘"]:
    print(q, "->", graph.invoke({"messages": [("user", q)]})["messages"][-1].content)
