import sys
from collections import deque
T = int(input())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    # [1:-1] 에서 -1은 배열의 맨 뒤 전까지를 의미한다.
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev = 0
    flag = 0
    if n == 0:
        queue = []

    for j in p:
        if j == "R":
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
