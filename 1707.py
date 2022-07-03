import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input())

def dfs(start, group):
    visited[start] = group # 해당 정점의 group 설정(1, -1)

    for i in graph[start]:
        if not visited[i]: # 만약 방문하지 않았다면
            a = dfs(i,-group) # 그룹 값을 -1 주어 dfs를 돈다.
            if not a: # 만약 a가 False이면
                return False 
        elif visited[i] == visited[start]: # 만약 현재 정점과 연결된 정점의 그룹 값이 같다면
            return False
    return True # 그 외 상황에는 True 값 반환

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False]*(V+1)
    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result:
                break
    print("YES" if result else "NO")