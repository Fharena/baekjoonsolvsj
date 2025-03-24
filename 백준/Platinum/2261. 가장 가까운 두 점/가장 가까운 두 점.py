import math
import sys

def dist(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    return x**2+y**2

input=sys.stdin.readline
n=int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()#x기준 오른차순으로 정렬


def sol(low,high): #점 번호 범위 넣으면


    if high==low: # 1개로 완전히 쪼개지면 선 못긋기 때문에 최댓값
        return 200000000#조건상 최댓값 좌표 절댓값이 10000
    elif high-low==1: #점 두개일때
        return dist(arr[low],arr[high])
    
    mid=(low+high)//2

    proximate=min(sol(low,mid),sol(mid+1,high))#양옆으로 재귀호출하며 최솟값으로 설정
    candidates = []
    for i in range(low, high+1):
        if (arr[mid][0] - arr[i][0])**2 < proximate:#x좌표가 proximate보다 작은경우만 집어넣음
            candidates.append(arr[i])
    candidates.sort(key=lambda x: x[1])
    for i in range(len(candidates)-1): #위에 모은점들끼리의 거리가 y좌표 차이가 proximate보다 작은경우만 거리계산해서 proximate보다작으면 대체
        for j in range(i+1, len(candidates)):
            if (candidates[i][1] - candidates[j][1])**2 < proximate:
                proximate = min(proximate,dist(
                    candidates[i], candidates[j]))
            else:
                break
    return proximate
print(sol(0,n-1))