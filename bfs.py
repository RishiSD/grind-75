

def bfs(graph, vertex):
    visited = set()
    queue = [vertex]
    while len(queue) > 0:
        vertex = queue.pop(0)
        if not vertex in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
            

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 2],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}

bfs(graph, 0)