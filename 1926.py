from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False] * m for _ in range(n)]


def bfs(x,y,count):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 < ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return count

answer = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i,j,0))

print(len(answer))
if not answer:
    print(0)
else:
    print(max(answer))
