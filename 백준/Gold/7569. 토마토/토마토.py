import sys
from collections import deque

input = sys.stdin.readline
#-1은 아예 처리 안하면 되는ㄱ거 아닌가?

graph=[]
dx = [0, 0, 1, -1,0,0]
dy = [1, -1, 0, 0,0,0]
dz = [0, 0, 0, 0, 1,-1]
M,N,H = map(int,input().split())
graph = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    graph.append(layer)
dq = deque()

def bfs():#토마토 익ㄱ는과정
    while dq:
        z, x, y =dq.popleft()
        for i in range(6):
            nx,ny,nz= x+dx[i],y+dy[i],z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H:
                if graph[nz][nx][ny]==0: #안익었으면 익게함
                    graph[nz][nx][ny] = graph[z][x][y]+1 #카운트 하나씩 올려가고, 마지막에 max하면 최대 걸린 날짜
                    dq.append((nz,nx,ny))



for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==1:
                dq.append((i,j,k))#큐에 1인것 다 넣기
bfs()#탐색시작

noend=0
day=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k]==0:
                noend=1
            else:
                day=max(day,graph[i][j][k])
if noend:
    print(-1)
else:
    print(day-1)#원래 0일차 1인 토마토에서 시작해서 -1
