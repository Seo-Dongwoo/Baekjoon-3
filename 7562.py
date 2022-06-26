from collections import deque
import sys
T = int(sys.stdin.readline())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(sx,sy,ax,ay):
    queue = deque()
    queue.append([sx,sy])
    graph[sx][sy] = 1
    while queue:
        a,b = queue.popleft()
        if a == ax and b == ay:
            print(graph[ax][ay] - 1)
            return
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                queue.append([nx,ny])
                graph[nx][ny] = graph[a][b] + 1

for _ in range(T):
    N = int(sys.stdin.readline())
    sx, sy = map(int,sys.stdin.readline().split())
    ax, ay = map(int,sys.stdin.readline().split())
    graph = [[0]*N for i in range(N)]
    bfs(sx,sy,ax,ay)