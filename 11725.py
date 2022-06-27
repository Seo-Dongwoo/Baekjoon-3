import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(N+1)]

def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = start
            dfs(i)
dfs(1)

for i in range(2, N+1):
    print(visited[i])