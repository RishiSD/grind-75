

def dfs(graph, vertex):
    visited = set()
    stack = [vertex]
    while len(stack) > 0:
        vertex = stack.pop()
        if not vertex in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
            

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 2],
    3: [1, 4, 5],
    4: [3],
    5: [3]
}

dfs(graph, 0)