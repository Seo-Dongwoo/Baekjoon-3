import sys
N = int(sys.stdin.readline())
line_list = []
for i in range(N):
    line_list.append(list(map(int, sys.stdin.readline().split())))

line_list.sort()
dp = [1]*N
for i in range(N):
    for j in range(i):
        if line_list[i][1] > line_list[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(N-max(dp))

