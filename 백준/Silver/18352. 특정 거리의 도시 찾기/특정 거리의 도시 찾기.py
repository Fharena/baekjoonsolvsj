
import sys,heapq
input = sys.stdin.readline
INF = float('inf')


N,M,K,X=map(int, input().split())#  도시갯수N, 도로갯수M, 최단거리정보K, 출발도시X
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, input().split())
    graph[a].append(b)


distance = [INF] * (N+1)
def dijikstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost =dist+1
            if cost<distance[i]:
                 distance[i]=cost
                 heapq.heappush(q,(cost,i))


dijikstra(X)
flag=1
for i in range(N+1):
    if distance[i]==K:
        print(i)
        flag=0

if flag:
    print(-1)
