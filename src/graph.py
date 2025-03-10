import networkx as nx
import matplotlib.pyplot as plt


# creating graph 
def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


# get degree 
def get_degree(G: nx.Graph, node: int) -> int:

    return G.degree(node)


#  dfs traversal 
def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
   
    return list(nx.dfs_preorder_nodes(G, start))


#  bfs traversal 
def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
   
    return list(nx.bfs_tree(G, start))


# finding shortest path 
def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:

    return nx.shortest_path(G, source, target)

# Draw the graph
def visualize_graph(G: nx.Graph, filename="graph.png") -> None:

    nx.draw(G)

    plt.savefig(filename)
    plt.show()
