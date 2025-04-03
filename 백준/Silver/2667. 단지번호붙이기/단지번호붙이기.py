import sys
input = sys.stdin.readline
dx=[0,0,-1,1]
dy=[-1,1,0,0]



N=int(input())

graph=[list(map(int, input().strip())) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
def dfs(x,y):
    global cnt
    cnt+=1
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and graph[nx][ny]==1:
            dfs(nx,ny)

group=0
cntgroup=[]
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and graph[i][j]==1:
            group+=1
            cnt=0
            dfs(i,j)
            cntgroup.append(cnt)
print(group)
cntgroup.sort()
print(*cntgroup,sep="\n")


