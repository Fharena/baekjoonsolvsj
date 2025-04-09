import sys
input=sys.stdin.readline
INF=16*10**6
dp={}
N=int(input())
city=[list(map(int,input().split()))for _ in range(N)]
#비트마스킹으로 체크. visited는 1일때 0001로 0번째 도시 방문처리.

def dfs(now,visited):
    if visited==(1<<N)-1:#16-1로 15가 되면 1111(2)
        if city[now][0]:#0으로 가는길 있으면 리턴주고 없으면 INF
            return city[now][0] #0으로 돌아와야댐
    
        else:
            return INF
    if (now,visited) in dp:#저장한값 있으면 dp에서 꺼내쓰기
        return dp[(now,visited)]
    min_cost = INF
    for next in range(N):
        if city[now][next] == 0 or visited & (1 << next):#거리가 0이거나 이미 방문헀으면
            continue#다음 도시로

        cost = dfs(next, visited | (1 << next)) + city[now][next]
        min_cost = min(cost, min_cost)#작은거 나올떄마다 갱신

    dp[(now, visited)] = min_cost  
    return min_cost
        


    

print(dfs(0,1))
