from queue_ import Queue
from stack import Stack

def BFS(graph, start):
    que = Queue()
    que.put(start)
    visited = [start]

    while not (que.isEmpty()):
        vert = que.get()

        for neighbor in graph[vert]:
            if neighbor not in visited:
                visited.append(neighbor)
                que.put(neighbor)
    
    return visited

def BFS_search(graph, start, goal):
    que = Queue()
    visited = [start]
    que.put([start])
    while not (que.isEmpty()):
        path = que.get()
        vert = path[-1]

        for neighbor in graph[vert]:
            if neighbor not in visited:
                if neighbor == goal:
                    path.append(neighbor)
                    return path
                else:
                    visited.append(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    que.put(new_path)
                    






        

def DFS(graph, start):
    visited = []
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        vert = stack.pop()
        visited.append(vert)
        for neighbor in reversed(graph[vert]):
            if (neighbor not in visited) and (neighbor not in stack.stack):
                stack.push(neighbor)
        
    return visited


def DFS_recursive(graph, vert, visited=[]):
    visited.append(vert)
    for neighbor in graph[vert]:
        if neighbor not in visited:
            DFS_recursive(graph, neighbor, visited)
    return visited



graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'B'],
    'E': ['A', 'B', 'F'],
    'F': ['C', 'E', 'G', 'H'],
    'G': ['F', 'H'],
    'H': ['F', 'G']
}

print(BFS_search(graph, 'D', 'F'))