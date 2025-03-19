routesum=[]
route=[]
p=0
N=int(input())
visited=[True]+[False]*(N-1)
W=[]
for i in range(N):
    W.append(list(map(int,input().split())))

def dfs(dep,current,cost):
    if dep==N-1:
        if W[current][0] != 0:  # 마지막 도시에서 출발 도시로 갈 수 있는지 확인
            routesum.append(cost + W[current][0])
        return
    for i in range(1, N):  # 0번 도시는 이미 방문했으므로 1부터 시작
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            dfs(dep + 1, i, cost + W[current][i])
            visited[i] = False  # 백트래킹

dfs(0,0,0)
print(min(routesum))