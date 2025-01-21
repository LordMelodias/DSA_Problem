def floyd_warshall(graph):
    nodes = list(graph.keys())
    print("Nodes: ", nodes)
    dist = {i: {j: graph[i][j] if j in graph[i] else float('inf') for j in nodes} for i in nodes}
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = {'A': {'A': 0, 'B': 3, 'C': 8}, 'B': {'A': 3, 'B': 0, 'C': 1}, 'C': {'A': 8, 'B': 1, 'C': 0}}
print("Shortest paths:", floyd_warshall(graph))


'''
Floyd-Warshall Algorithm
Definition: A dynamic programming algorithm to find the shortest paths between all pairs of nodes in a graph.
Objective: Minimize the cost between any two nodes.
Diagram:
mathematica
Copy
Edit
Graph:
  A--3--B--1--C
       \    /
        6
'''