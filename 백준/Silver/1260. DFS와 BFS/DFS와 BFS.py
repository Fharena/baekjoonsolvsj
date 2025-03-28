import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def DFS(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:#소팅해서 start부터 쭉
        if not visited[i]:#방문체크
            DFS(i)
def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:#큐에는 제거한 v와 연결된 노드중(그래프에 저장한) 이미 방문한것들은 제외하고 전부 추가->이러면 방문할 순서대로 큐에 저장됨
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N,M,V=map(int,input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
visited = [False] * (N + 1)
DFS(V)
print()
visited = [False] * (N + 1)
BFS(V)
