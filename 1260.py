import sys
from collections import deque
def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start): # BFS 선언
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [0] *(N+1)
dfs(V)
print()
visited = [0] *(N+1)
bfs(V)