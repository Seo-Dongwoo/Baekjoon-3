import sys
from collections import deque
input = sys.stdin.readline
N, L , R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    # 연합에 가입한 나라 list
    country = []
    # 나라 인구수의 합
    people = 0
    queue = deque()
    queue.append((x,y))
    country.append((x,y))
    people += graph[x][y]
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    queue.append((nx,ny))
                    country.append((nx,ny))
                    people += graph[nx][ny]
                    visited[nx][ny] = True
    newPeople = people // len(country)

    for x, y in country:
        graph[x][y] = newPeople

    return True if len(country) > 1 else False


day = 0
while True:
    visited = [[-1]*(N) for _ in range(N)]
    stop = True # stop이 True이면 while문 종료
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                check = bfs(i,j)
                if check:
                    stop = False

    if stop:
        break
    else:
        day += 1
print(day)
