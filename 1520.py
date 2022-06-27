import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(sx,sy):
    # 도착 지점에 도달하면 1을 리턴
    if sx == M-1 and sy == N-1:
        return 1
    # 이미 방문했다면 그 위치에서 출발하는 경우의 수 리턴
    if dp[sx][sy] != -1:
        return dp[sx][sy]
    ways = 0
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        # graph[sx][sy] > graph[nx][ny]는 출발 위치가 더 클 경우 진행
        if 0 <= nx < M and 0 <= ny < N and graph[sx][sy] > graph[nx][ny]:
            ways += dfs(nx,ny)

    dp[sx][sy] = ways
    return dp[sx][sy]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1]*N for _ in range(M)]
print(dfs(0,0))