import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


K=int(input())

def dfs(v):
    global no
    if visited[v]==1:
        for i in graph[v]:
            if visited[i]==1:
                no=1
            elif visited[i]==0:
                visited[i]=-1
                dfs(i)
    else :
        for i in graph[v]:
            if visited[i]==-1:
                no=1
            elif visited[i]==0:
                visited[i]=1
                dfs(i)

        

for _ in range(K):#테스트케이스
    no=0
    V,E=map(int,input().split())
    graph = [[] for _ in range(V + 1)]
    visited=[0]*(V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited[1]=1
    for i in range(1, V + 1):
        dfs(i)
    if no==1:
            print("NO")
    else:
        print("YES")


