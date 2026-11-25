from utils.nodes import create_analyst
from langgraph.graph import START, END, StateGraph
from utils.states import GenerateAnalystsState
from dotenv import load_dotenv

load_dotenv()

# Creating the graph

builder = StateGraph(GenerateAnalystsState)

# Adding Nodes to the Graph
builder.add_node("create_analysts", create_analyst)

# Adding Edges to the Graph
builder.add_edge(START, "create_analysts")
builder.add_edge("create_analysts", END)

graph = builder.compile()