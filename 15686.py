from itertools import combinations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            house.append((i,j))
        elif map[i][j] == 2:
            chicken.append((i,j))
minv = float('inf')
for ch in combinations(chicken,M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        if minv <= sumv:
            break
    if sumv < minv:
        minv = sumv
print(minv)