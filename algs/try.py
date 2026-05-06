def dijkstra(graph, start):
    distances = {vertex: {'dist': float('infinity'), 'path': ""} for vertex in graph}
    distances[start]['dist'] = 0
    distances[start]['path'] = start
    unvisited = set(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda v: distances[v]['dist'])
        current_distance = distances[current_vertex]['dist']
        current_path = distances[current_vertex]['path']

        
        if current_distance == float('infinity'):
            break

        unvisited.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight
            new_path = current_path + neighbor
            if new_distance < distances[neighbor]['dist']:
                distances[neighbor]['dist'] = new_distance
                distances[neighbor]['path'] = new_path

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))