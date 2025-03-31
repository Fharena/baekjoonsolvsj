import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
N,M = map(int,input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

around_sea = [[0] * M for _ in range(N)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def melt(x,y): # 인접해있는 칸 수 확인하기
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if nx<0 or ny<0 or nx>=N or ny>=M:
            continue
        if graph[nx][ny]==0:
            around_sea[x][y]+=1

def dfs(i,j):#이거로 붙은거 찾기.이후 main에서 cnt에 하나 끝날때마다 cnt+=1
    visited[i][j]=1

    for t in range(4):
            nx = i + dx[t]
            ny = j + dy[t]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny]!=0 and visited[nx][ny]==0:
                dfs(nx,ny)

year = 0

while True:
    cnt=0
    ice=0
    year += 1
    visited= [[0] * M for _ in range(N)]
    for i in range(N): # 바닷물 인접 개수 구하기
        for j in range(M):
            if graph[i][j] > 0:
                ice += 1
                melt(i,j) 
    if ice == 0: 
        print(0)
        break
    for i in range(N):#얼음 녹이기
        for j in range(M):
            if graph[i][j] > around_sea[i][j]:
                graph[i][j]-=around_sea[i][j]
                around_sea[i][j] = 0 # 녹이고 다시 초기화
            else:
                graph[i][j] = 0
                around_sea[i][j] = 0 

    for i in range(N): # 덩어리의 개수 구하기
        for j in range(M):
            if graph[i][j]>0 and visited[i][j]==0:
                dfs(i,j)
                cnt+=1
    if cnt>=2:
        print(year)
        break