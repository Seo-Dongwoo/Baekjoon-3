import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
dp = [0 for i in range(k+1)]
dp[0] = 1
for i in arr:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])