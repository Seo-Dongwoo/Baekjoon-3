n, k = map(int, input().split())  # n: 물품의 수, k: 가방에 넣을 수 있는 최대 무게
dp = [[0] * (k+1) for _ in range(n+1)]
m = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())  # w: 각 물건의 무게, v: 물건의 가치
    m.append([w, v])

for i in range(1, n+1):
    w = m[i][0]
    v = m[i][1]
    for j in range(1, k+1):
        # 가방 무게 < 물건 무게 이라면
        if j < w:
            # 이전 물건 빼지 않고 그대로
            dp[i][j] = dp[i-1][j]
        else:
            # 현재 물건 가치 + [이전 물건][가방-물건] , [이전 물건][현재 가방]
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[n][k])
