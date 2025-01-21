import heapq

def prims(graph, start):
    mst = []
    visited = set()
    pq = [(0, start)]
    while pq:
        cost, node = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            mst.append((node, cost))
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (weight, neighbor))
    return mst

graph = {'A': {'B': 1, 'C': 3}, 'B': {'A': 1, 'C': 2}, 'C': {'A': 3, 'B': 2}}
print("MST:", prims(graph, 'A'))



'''
Minimum Cost Spanning Tree (Prim's Algorithm)
Definition: A greedy algorithm to connect all nodes in a graph with the minimum total edge weight without forming a cycle.
Objective: Minimize the total weight of the tree.
Diagram:
mathematica
Copy
Edit
Graph:
  A---1---B---2---C
  |       |
  3       4
  D-------E
'''