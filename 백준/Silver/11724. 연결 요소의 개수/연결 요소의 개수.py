import sys
input = sys.stdin.readline

N,M=map(int,input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N + 1)

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] !=True:
            dfs(i)
cnt=0
for j in range(1,N+1):
    if visited[j] !=True:
        cnt+=1
        dfs(j)
print(cnt)