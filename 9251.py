import sys
A = sys.stdin.readline().strip().upper()
B = sys.stdin.readline().strip().upper()

lcs = [[0]*(len(A)+1) for _ in range(len(B) +1)]

for i in range(1,len(B)+1):
    for j in range(1, len(A)+1):
        if A[i-1] == B[j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
print(lcs[-1][-1])
