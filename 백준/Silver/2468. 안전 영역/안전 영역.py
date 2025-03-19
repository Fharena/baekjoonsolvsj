from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]## 건물정보
max_rain = max(map(max, graph))



dx=[0,-0,-1,1]
dy=[1,-1,0,0]
def bfs(i,j):#sink값이 False인 안잠긴 좌표 하나씩 집어넣기
    global cnt
    q=deque()
    q.append((i,j))#q에 좌표 집어넣고
    sink[i][j]=True # 확인겸 잠겼다고 하기
    cnt+=1 #구역의 첫번째 좌표므로 카운트+1
    while q: #q가 존재하면
        x,y=q.popleft()#먼저 넣은 q값부터 제거하고 x,y에 집어넣고 현재 확인할 값의 좌표 기억
        for i in range(4):# 상하좌우 이동
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:#도시의 경계 밖으로 나갈경우 아무것도 안함
                continue
            if sink[nx][ny] == False:#안나간 경우는 상하좌우로 이동한 좌표가 잠기지 않았다면 q에 넣고 잠겼다고 하기
                q.append((nx,ny))#q에 좌표 집어넣고
                sink[nx][ny]=True # 확인겸 잠겼다고 하기

countlist=[]
for rain in range(max_rain):# max_rain이전까지의 비왔을 경우로 sink 채우기
    cnt=0#카운트 초기화
    sink = [[False for _ in range(N)] for _ in range(N)] #일단 전부 안잠긴상태로 sink 생성
    for i in range(N):
        for j in range(N):
            if graph[i][j]<=rain:
                sink[i][j]=True  #비왔을 경우로 sink 채우기
    for i in range(N):
        for j in range(N): 
            if sink[i][j]==False:
                bfs(i,j)
    countlist.append(cnt)
print(max(countlist))

