import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
cnt = [[INF] * N for _ in range(N)]
cnt[0][0] = 0

dq = deque()
dq.append((0, 0))

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            # 흰 방일 경우 (1): 비용 없이 이동 → 앞에 넣기
            if graph[nx][ny] == '1' and cnt[nx][ny] > cnt[x][y]:
                cnt[nx][ny] = cnt[x][y]
                dq.appendleft((nx, ny))
            # 검은 방일 경우 (0): 벽을 부수고 이동 → 뒤에 넣기
            elif graph[nx][ny] == '0' and cnt[nx][ny] > cnt[x][y] + 1:
                cnt[nx][ny] = cnt[x][y] + 1
                dq.append((nx, ny))

print(cnt[N-1][N-1])
