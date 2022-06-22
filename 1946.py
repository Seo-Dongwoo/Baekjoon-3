import sys
T = int(sys.stdin.readline())
for i in range(0, T):
    cnt= 1
    people=[]
    N = int(sys.stdin.readline())
    for i in range(N):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper,interview])

    people.sort()
    Max = people[0][1]

    for i in range(1,N):
        if Max > people[i][1]:
            cnt += 1
            Max = people[i][1]

    print(cnt)