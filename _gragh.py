gragh_nodir = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

gragh_dir = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0]
]

gragh_list = [
    [0, 1, 4],
    [1, 0, 2, 3],
    [2, 1, 3],
    [3, 1, 2],
    [4, 0]
]

visited = [0] * len(gragh_nodir)

def dfs_matrix(i):
    visited[i] = 1
    print i
    for c, v in enumerate(gragh_dir[i]):
        if v == 1 and visited[c] == 0:
            dfs_matrix(c)

def dfs_list(i):
    visited[i] = 1
    print i
    for i in gragh_list[i][1:]:
        if visited[i] == 0:
            dfs_list(i)

def bfs_matrix():
    queue = [0]
    visited[0] = 1
    while queue:
        n = queue.pop()
        print n
        for i, v in enumerate(gragh_nodir[n]):
            if v == 1 and visited[i] == 0:
                visited[i] = 1
                queue.insert(0, i)

def bfs_list():
    queue = [0]
    visited[0] = 1
    while queue:
        n = queue.pop()
        print n
        for i in gragh_list[n][1:]:
            if visited[i] == 0:
                visited[i] = 1
                queue.insert(0, i)

dfs_matrix()