from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools import TOOLS

load_dotenv()
llm = init_chat_model("openai:gpt-4o-mini").bind_tools(TOOLS)

def agent(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}

g = StateGraph(MessagesState)
g.add_node("agent", agent)
g.add_node("tools", ToolNode(TOOLS))
g.add_edge(START, "agent")
g.add_conditional_edges("agent", tools_condition)
g.add_edge("tools", "agent")
graph = g.compile()

if __name__ == "__main__":
    print(graph.get_graph().draw_mermaid())
    out = graph.invoke({"messages": [("user", "5명 회의실 찾아줘")]}, {"recursion_limit": 10})
    print(out["messages"][-1].content)
