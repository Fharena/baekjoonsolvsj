import sys
input = sys.stdin.readline


N=int(input())
insideout=list(input().strip())
inout=[0]
for i in insideout:
    inout.append(int(i))


graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    global cnt
    visited[v]=1

    for i in graph[v]:
        if visited[i]==0:
            if inout[i]==1:
                visited[i]=1
                cnt+=1

            else:
                dfs(i)

cnt=0
for i in range(1,N+1):
    if inout[i]==1:
        
        visited = [0]*(N+1) 
        dfs(i)
print(cnt)