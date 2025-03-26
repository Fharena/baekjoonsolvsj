import sys
from collections import deque
input = sys.stdin.readline

N,K=map(int,input().split())
Nlist=[]

queue=deque(range(1,N+1))

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    Nlist.append(queue.popleft())

print(f"<{', '.join(list(map(str, Nlist)))}>")