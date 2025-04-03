import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
M= int(input())
cnt=[[0]*(N+1) for _ in range(N+1)]#개수세기
graph=[[] for _ in range(N+1)]

indegree=[0]*(N+1) #진입차수

for _ in range(M):#그래프에 각 노드 이동방향 저장
    a,b,c,= map(int, input().split())
    graph[b].append((a,c))
    indegree[a]+=1

q=deque([])
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:  #정렬
    now=q.popleft()
    for a, c in graph[now]:
        if cnt[now].count(0) == N + 1:#최소단위 부품일때.
            cnt[a][now] += c #다음부품에 자기자신 위치에 개수++
        else:
            for i in range(1, N + 1):
                cnt[a][i] += cnt[now][i] * c

        indegree[a] -= 1
        if indegree[a] == 0:
            q.append(a)
for x in enumerate(cnt[N]):
    if x[1] > 0:
        print(*x)