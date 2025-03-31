from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
pan = [list(str(input().strip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
distance = [[1 for _ in range(M)] for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny < 0 or nx>=N or ny >= M or pan[nx][ny] == '0':
                continue
            if visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                distance[nx][ny] += distance[x][y]

bfs()
print(distance[N-1][M-1])