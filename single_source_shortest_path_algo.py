import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, node = heapq.heappop(pq)
        for neighbor, weight in graph[node].items():
            distance = curr_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist

graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 6}, 'C': {}, 'D': {}}
print("Shortest distances:", dijkstra(graph, 'A'))


'''
Single Source Shortest Path Algorithm (Dijkstra's)
Definition: Finds the shortest path from a source node to all other nodes in a graph.
Objective: Minimize the total cost of paths.
Diagram:
mathematica
Copy
Edit
Graph: A--1--B--2--C
               |
               3
               D
'''