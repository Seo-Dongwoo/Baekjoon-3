T = int(input())
time = [300, 60, 10]
ans = []
count = 0
if T % 10 != 0:
    print(-1)
else:
    for i in time:
        count = T // i
        ans.append(count)
        T %= i
    print(ans[0],ans[1],ans[2],sep=' ')