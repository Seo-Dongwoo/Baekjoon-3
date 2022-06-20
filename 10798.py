s = [[0]*15 for i in range(5)]

for i in range(5):
    d = list(input())
    for j in range(len(d)):
        s[i][j] = d[j]
for i in range(15):
    for j in range(5):
        if s[j][i] != 0:
            print(s[j][i], end="")
        else:
            continue