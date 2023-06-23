import sys

sys.setrecursionlimit(10**6)


def dfs(graph, v, seen):
    seen[v] = True
    for next in graph[v]:
        if seen[next]:
            continue
        dfs(graph, next, seen)
    print(v)


N = 4
graph = [[] for _ in range(N)]
graph[0] = [1]
graph[1] = [0, 2, 3]
graph[2] = [1]
graph[3] = [1]
seen = [False for _ in range(N)]
dfs(graph, 0, seen)
