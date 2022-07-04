import sys
sys.setrecursionlimit(10**9)

def dfs(start_node, current_wei):
    for a, b in graph[start_node]:
        if visited[a] == -1:
            visited[a] = b + current_wei
            dfs(a, b + current_wei)

V = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
for _ in range(V):
    w = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(w) - 2, 2):
        graph[w[0]].append([w[j], w[j + 1]])

visited = [-1] * (V + 1) # 탐색 여부, 간선의 거리
visited[1] = 0
dfs(1, 0) # 1번 노드에서 dfs 탐색

first_far_node = visited.index(max(visited)) # 1번 노드에서 제일 먼 노드를 찾는다.

visited = [-1] * (V + 1)
visited[first_far_node] = 0
dfs(first_far_node, 0) # 1번 노드부터 가장 먼 노드에서 다시 제일 먼 노드를 찾는다.
print(max(visited))
