from dotenv import load_dotenv

from langgraph.graph import START, END, StateGraph

from utils.states import GenerateAnalystsState
from utils.nodes import create_analyst, human_feedback
from utils.edges import should_continue

load_dotenv()

# Creating the graph

builder = StateGraph(GenerateAnalystsState)

# Adding Nodes to the Graph
builder.add_node("create_analysts", create_analyst)
builder.add_node("human_feedback",human_feedback )

# Adding Edges to the Graph
builder.add_edge(START, "create_analysts")
builder.add_edge("create_analysts", "human_feedback")
builder.add_conditional_edges("human_feedback", should_continue)

graph = builder.compile()