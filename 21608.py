import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
# 좋아하는 학생 리스트를 likedict에 저장
likedict = defaultdict(list)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 교실 설정
graph = [[0 for _ in range(N)] for _ in range(N)]

result = 0

for _ in range(N*N):
    a = list(map(int, input().split()))
    # index 1번부터가 좋아하는 학생들
    likedict[a[0]] = a[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1
    # graph를 돌면서 인전한 칸의 좋아하는 학생 수와 비어있는 칸을 센다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] in a:
                            likecnt += 1
                        if graph[nx][ny] == 0:
                            emptycnt += 1

                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x = i
                    max_y = j
                    max_like = likecnt
                    max_empty = emptycnt
    graph[max_x][max_y] = a[0]

for i in range(N):
    for j in range(N):
        cnt = 0
        like = likedict[graph[i][j]]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] in like:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt-1)
print(result)