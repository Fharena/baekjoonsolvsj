

import sys
input = sys.stdin.readline

N,M=map(int,input().split())
visited=[[0]*M for _ in range(N)]
graph=[list(input().strip())for _ in range(N)]


def search(x,y):

    visited[x][y]=1
    if graph[x][y]=='-':
        ny=y+1
        if ny < M  and graph[x][ny]=='-' and visited[x][ny] == 0:
            search(x,ny)
    
    elif graph[x][y]=='|':
        nx=x+1
        if nx < N and graph[nx][y] == '|' and visited[nx][y] == 0:
            search(nx,y)

cnt=0
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            cnt+=1
            search(i,j)

print(cnt)
