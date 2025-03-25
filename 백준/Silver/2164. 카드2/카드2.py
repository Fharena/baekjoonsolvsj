import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
queue=deque([])
for i in range(1,N+1):
    queue.append(i)
if len(queue)==1:
    print(1)

while len(queue)>=2:
    queue.popleft()
    if len(queue)==1:
        print(queue[0])
        break
    movecard=queue.popleft()
    queue.append(movecard)
