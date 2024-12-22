

def dfs(graph, vertex, visited):
    print(vertex, end=' ')
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

visited = set()
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 2],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}

dfs(graph, 0, visited)