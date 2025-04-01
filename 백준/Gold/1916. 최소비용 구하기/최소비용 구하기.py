
import sys,heapq
input = sys.stdin.readline
INF=float('inf')
N=int(input())
M=int(input())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())

distance=[INF for _ in range(N+1)]
def dijikstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist>distance[now]:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijikstra(start)

print(distance[end])

