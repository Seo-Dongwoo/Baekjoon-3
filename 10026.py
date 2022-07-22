from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N = int(input())

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
                    

graph = [list(map(str, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
# 적록색약이 없는 경우
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')

# 적록색약이 있을 경우
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"
visited = [[0]*N for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt += 1
print(cnt)