import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1# 진입차수 추가

q = deque()

for s in range(1, N+1):
    if inDegree[s] == 0:
        q.append(s)

ans = []

while q:
    s = q.popleft()
    ans.append(s)
    
    for i in graph[s]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            q.append(i)

print(*ans, sep=" ")