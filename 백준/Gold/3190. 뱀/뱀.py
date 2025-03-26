import sys
from collections import deque
input = sys.stdin.readline
apple=[]
direction_change=[]
direcsec=0
direction=0#방향

snake=deque([(0,0)])

N=int(input())
K=int(input())
for _ in range(K):
    x, y = map(int, input().split())
    apple.append((x-1, y-1))
L=int(input())
for _ in range(L):
    x, y = input().split()
    direction_change.append((int(x), y))
sec=0
change=[(0,1),(1,0),(0,-1),(-1,0)]
x=0#머리 위치
y=0

while True:
    
    sec+=1
    nx = x + change[direction][0]
    ny = y + change[direction][1]

    #자기 몸이나 벽에 부딛히면 break
    if not (0 <= nx < N and 0 <= ny < N) or (nx, ny) in snake:
        break

    snake.append((nx, ny))

    if (nx, ny) in apple:#이동한 자리에서 사과 먹을때는 뒤에 안줄음
        apple.remove((nx, ny))
    else:
        snake.popleft()
     
    if direcsec < len(direction_change) and sec==direction_change[direcsec][0]:#시간초와 방향전환 시간초 같을시
        
        if direction_change[direcsec][1]=='D':# 방향 바꾸기
            direction=(direction+1)%4
        elif direction_change[direcsec][1]=='L':
            direction = (direction - 1) % 4
        direcsec+=1#다음 방향전환으로 이동
    x, y = nx, ny
     

print(sec)