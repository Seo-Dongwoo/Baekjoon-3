from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visited = [0] *(N+1)
def bfs(graph,start):
    global cnt
    queue = deque([start])
    while queue:
        node = queue.popleft()
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    print(cnt)
bfs(graph,1)