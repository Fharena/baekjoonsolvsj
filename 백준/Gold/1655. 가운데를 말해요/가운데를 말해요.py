import sys #정렬하지 말고 애초부터 들어갈때 비교하면서 정렬된것을 완성
import heapq
input = sys.stdin.readline
N = int(input())
leftheap=[]#양쪽으로 하나씩 숫자 주기
rightheap=[]
for _ in range(N):
    num=int(input())

    if len(leftheap)==len(rightheap):
        heapq.heappush(leftheap,-num)
    else:
        heapq.heappush(rightheap,num)

    if rightheap and rightheap[0]<-leftheap[0]:
        
        leftval=heapq.heappop(leftheap)
        rightval=heapq.heappop(rightheap)

        heapq.heappush(leftheap,-rightval)
        heapq.heappush(rightheap,-leftval)
    
    print(-leftheap[0])
