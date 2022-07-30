import sys
from collections import deque
N, Q = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = (map(int, sys.stdin.readline().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    visited = [False]*(N+1)
    visited[v] = True
    result = 0
    queue = deque([(v, float('inf'))])

    while queue:
        v, usado = queue.pop()
        for next_v, next_usado in graph[v]:
            next_usado = min(usado, next_usado)
            if next_usado >= k and not visited[next_v]:
                result += 1
                queue.append((next_v, next_usado))
                visited[next_v] = True
    print(result)
