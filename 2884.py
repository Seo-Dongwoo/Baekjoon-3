H, M = map(int, input().split())
if 45 <= M:
    print(H, M-45)
elif M < 45 and H > 0:
    print(H-1, 15+M)
else:
    print(23, 15+M)