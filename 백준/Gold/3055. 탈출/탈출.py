import sys
from collections import deque
input = sys.stdin.readline

R,C= map(int,input().split())

graph=[list(input().strip()) for _ in range(R)]
distance = [[0] *C for _ in range(R)] #이동거리(시간)저장

dx=[0,0,-1,1]
dy=[-1,1,0,0]
dq=deque([])


def bfs():
    while dq:
        x,y= dq.popleft()
        if graph[Dx][Dy]=='S':# 비버집 도착하면 집까지의 거리 리턴
            return distance[Dx][Dy]
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[x][y]=='S' and (graph[nx][ny]=='.'or graph[nx][ny]=='D'):
                    graph[nx][ny]='S'
                    distance[nx][ny]=distance[x][y]+1
                    dq.append((nx,ny))
                if graph[x][y]=='*' and (graph[nx][ny]=='.'or graph[nx][ny]=='S'):
                    graph[nx][ny]='*'
                    dq.append((nx,ny))
    return "KAKTUS"

for i in range(R):
    for j in range(C):
        if graph[i][j]=='S':
            dq.append((i,j))
        elif graph[i][j]=='D':
            Dx,Dy=i,j

for i in range(R):
    for j in range(C):
        if graph[i][j]=='*':
            dq.append((i,j))


print(bfs())