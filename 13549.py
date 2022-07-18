from collections import deque
def bfs(N):
    visited = [0]*100001
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for next_x in (x+1,x-1,x*2):
            if 0 <= next_x < 100001:
                if visited[next_x] == 0:
                    if next_x == x * 2 and next_x != 0:
                        visited[next_x] = visited[x]
                        queue.appendleft(next_x)
                    else:
                        visited[next_x] = visited[x] + 1
                        queue.append(next_x)

N, K = map(int, input().split())
answer = bfs(N)
print(answer)