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



def DFS(tree, start, visited=[]):
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
        for node in tree[start]:
           DFS(tree, node, visited)

DFS(tree, 'A')