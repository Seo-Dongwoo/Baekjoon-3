import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = int(1e9)
graph = [[INF] * (N+1) for i in range(N+1)]
for a in range(1,N+1):
    for b in range(1,N+1):
        if a == b:
            graph[a][b] = 0

for i in range(M):
    s,e,c = map(int, input().split())
    if graph[s][e] > c:
        graph[s][e] = c

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
          if a == b:
              graph[a][b] = 0
          else:
              graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b],end=" ")
    print()