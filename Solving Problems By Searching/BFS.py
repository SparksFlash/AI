tree = {
    'A':['B','E'],
    'B':['C','D'],
    'C':['F'],
    'D':[],
    'E':['G','H'],
    'F': [],
    'G':[],
    'H':[]
}




from collections import deque
def BFS(tree, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


BFS(tree, 'A')