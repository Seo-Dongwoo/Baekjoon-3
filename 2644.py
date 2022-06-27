import sys
input = sys.stdin.readline

def dfs(current_node):
    for i in graph[current_node]:
        if visited[i] == 0:
            visited[i] = visited[current_node] + 1
            dfs(i)

N = int(input())
target_start, target_end = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[target_start] = 0
dfs(target_start)
print(visited[target_end] if visited[target_end] > 0 else - 1)