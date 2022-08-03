import sys
import heapq
N, K = map(int, sys.stdin.readline().split())
diaList = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
diaList.sort()
bagList.sort()
result = 0
temp = []

for bagWeight in bagList:
    while diaList and bagWeight >= diaList[0][0]:
        heapq.heappush(temp, -diaList[0][1])
        heapq.heappop(diaList)

    if temp:
        result += heapq.heappop(temp)
    elif not diaList:
        break

print(-result)