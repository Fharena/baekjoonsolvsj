import sys
import heapq
input=sys.stdin.readline
n=int(input())
h = [sorted(map(int, input().split())) for _ in range(n)]## 집이던 사무실이던 더 가까운게 앞으로 가게
d=int(input())
heap=[]
sorted_h= sorted(h,key=lambda x : (x[1]))

maxcnt=0
for i in range(0,n):
    heapq.heappush(heap,sorted_h[i][0])
    lstart=sorted_h[i][1]-d
    while heap and heap[0] < lstart:#힙이 존재하고 최소힙에 들어온 start가 가장 작은개체부터 나감
        heapq.heappop(heap)
    if maxcnt<len(heap):
        maxcnt=len(heap)

print(maxcnt)