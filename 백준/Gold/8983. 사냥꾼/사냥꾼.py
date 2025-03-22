import sys
input=sys.stdin.readline
cnt=0
M,N,L=map(int,input().split())
X=list(map(int,input().split()))
X.sort()
animal=list(list(map(int,input().split())) for _ in range(N))
def dis(a,b,X):
    return abs(X-a)+b

def binary_search(a,b):#N개의 사대중에서 거리안에 들어가는지 이진탐색
    global cnt
    low=0
    high=M-1
    while low<=high:
        mid=(low+high)//2
        if dis(a,b,X[mid])<=L:
            cnt+=1
            return

        elif X[mid]>a:
            high=mid-1
        else:
            low=mid+1
    return
for a, b in animal:
    if b > L:
        continue
    binary_search(a, b)

print(cnt)


