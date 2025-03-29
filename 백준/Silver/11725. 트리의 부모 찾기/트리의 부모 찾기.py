import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0]*(N+1) 
def dfs(v):
    for i in graph[v]:
        if visited[i]==0:
            visited[i]=v
            dfs(i)

dfs(1)

for j in range(2,N+1):
    print(visited[j])

