graph = {'A': ['B', 'C', 'D'],
         'B': ['E','F', 'G'],
         'C': ['H', 'I', 'J'],
         'D': ['K', "L", "M"],
         'E': ['N','O', 'P'],
         'F': ['Q'],
         'G': ['R'],
         'H': ["S"]}

def bfs(graph, initial):
    visited = []
    queue = [initial]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue+=graph.get(node, [])
    return visited
 
print(bfs(graph,'A'))