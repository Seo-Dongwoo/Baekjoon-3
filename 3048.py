N, M = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
path = ant1[::-1] + ant2
T = int(input())
for _ in range(T):
    for i in range(len(path) - 1):
        if path[i] in ant1 and path[i+1] in ant2:
            path[i], path[i+1] = path[i+1], path[i]

            if path[i+1] == ant1[0]:
                break
print(''.join(path))