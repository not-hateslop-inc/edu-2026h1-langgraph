import sys; sys.path.append("week8")
from langgraph.checkpoint.memory import InMemorySaver
from importlib import import_module

g = import_module("03_state_graph").g
graph = g.compile(checkpointer=InMemorySaver())
cfg = {"configurable": {"thread_id": "demo"}}
print(graph.invoke({"messages": [("user", "8명 회의실 찾아줘")]}, cfg)["messages"][-1].content)
print(graph.invoke({"messages": [("user", "그 방 이름이 뭐였지?")]}, cfg)["messages"][-1].content)
