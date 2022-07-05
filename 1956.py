import sys
INF = int(1e9)
V, E = map(int, sys.stdin.readline().split())
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c, = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 모든 정점에서 모든 정점으로 가는 최소 거리
for i in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 자기 자신 => 자기 자신 마을로 돌아오는 최소 거리
result = INF
for i in range(1, V+1):
    result = min(result, graph[i][i])
if result == INF:
    print(-1)
else:
    print(result)
            