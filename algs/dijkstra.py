def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda v: distances[v])
        current_distance = distances[current_vertex]

        
        if current_distance == float('infinity'):
            break

        unvisited.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))