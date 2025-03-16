import graph as g

edge = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 9), (6, 10), (7, 11), (8, 12), (9, 12), (10, 12), (11, 12)]

graph = g.create_graph(edge)
dfs_result = g.dfs_traversal(graph, 4)
bfs_result = g.bfs_traversal(graph, 3)
path = g.find_shortest_path(graph, 2, 8)
degree = g.get_degree(graph, 7)

#print the result
print("Graph Nodes:", graph.nodes)
print("DFS Traversal:", dfs_result)
print("BFS Traversal:", bfs_result)
print("Shortest Path:", path)
print("Degree of node 7:", degree)


g.visualize_graph(graph, "graph.png")

