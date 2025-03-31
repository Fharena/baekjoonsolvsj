import sys
input = sys.stdin.readline
N, M = map(int, input().split())

heavy_list = [[] for _ in range(N+1)]
light_list = [[] for _ in range(N+1)]

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_list[heavy].append(light)
    light_list[light].append(heavy)


def DFS(list, root):
    count = 0
    for node in list[root]:
        if not visited[node]:
            visited[node] = True
            count += 1
            count += DFS(list, node)
    return count


mid = (N+1)/2
result = 0

for root in range(1, N+1):
    visited = [False] * (N+1)
    if DFS(heavy_list, root) >= mid:
        result += 1
    elif DFS(light_list, root) >= mid:
        result += 1

print(result)