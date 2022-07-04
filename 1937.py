import sys
sys.setrecursionlimit(10**6)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[x][y] < graph[nx][ny]:
           dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)
    return dp[x][y]

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[False]*N for _ in range(N)]
count = 0

for i in range(N):
    for j in range(N):
        count = max(count, dfs(i, j))
print(count)

