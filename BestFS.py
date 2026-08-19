graph={
    'A':['B','C','D'],
    'B':[],
    'C':['E','F'],
    'D':['H'],
    'E':[],
    'F':['G'],
    'G':[],
    'H':[]   
}

h={
    'A':6,
    'B':5,
    'C':3,
    'D':4,
    'E':6,
    'F':2,
    'G':0,
    'H':7
}
start='A'
goal='G'
queue=[start]
visited=[]

while queue:
    node=min(queue, key=lambda x: h[x])
    queue.remove(node)

    if node not in visited:
        print(node,end=" ")
        visited.append(node)

        if node ==goal:
            print("\nGoal Reached!")
            break

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
