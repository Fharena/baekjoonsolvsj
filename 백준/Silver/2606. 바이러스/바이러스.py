import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

cnt = 0
visited = [False] * (N + 1)

def dfs(start):
    global cnt
    visited[start] = True
    cnt += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(cnt - 1)
