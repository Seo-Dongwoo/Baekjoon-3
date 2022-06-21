N = int(input())
s = list(map(int, input().split()))
s.sort()
result = 0
for i in range(N):
    for j in range(i+1):
        result += s[j]
print(result)