import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())
insideout=list(input().strip())
inout=[0]
for i in insideout:
    inout.append(int(i))


graph = [[] for _ in range(N + 1)]
visited = [0]*(N+1) 
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    k=0
    visited[v]=1

    for i in graph[v]:
        if visited[i]==0:
            if inout[i]==0:
                visited[i]=1
                k+=dfs(i)

            else:
                k+=1
    return k


cnt=0
for i in range(1,N+1):
    if inout[i]==1:
        for j in graph[i]:
            if inout[j]==1:
                cnt+=1
                continue


    if inout[i]==0:
        if not visited[i]:
            k=dfs(i)
            cnt+=(k*(k-1))
print(cnt)
