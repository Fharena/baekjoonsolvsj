import sys
input=sys.stdin.readline
from collections import deque

T=int(input())


for _ in range(T):
    N,M=map(int,input().split())
    queue=deque([])
    cnt=0
    a = list(map(int, input().split()))
    for i in range(N):
        queue.append((i, a[i]))
    
    while queue:
        poped=queue.popleft()
        if any(poped[1]<importance[1] for importance in queue):#하나라도 큰거 있으면
            queue.append(poped)
            continue
        cnt+=1
        if poped[0]==M:
            print(cnt)

