n = int(input())
cards = set(map(int, input().split(' ')))

m = int(input())
targets = list(map(int, input().split(' ')))

for i in targets:
    if i in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')