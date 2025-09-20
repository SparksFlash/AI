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



def DFS_LIMITED(tree, start, limit, visited=[]):
    if limit <= 0:
        return
    if start not in visited:
        print(start, end=" ")
        visited.append(start)
    for node in tree[start]:
        DFS_LIMITED(tree, node, limit-1, visited)

DFS_LIMITED(tree, 'A', 3)