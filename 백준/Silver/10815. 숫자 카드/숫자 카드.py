import sys
input=sys.stdin.readline
N=int(input())
cardN=list(map(int,input().split()))

M=int(input())
numM=list(map(int,input().split()))
cardN.sort()


def binary_search(num):
    start=0
    end=len(cardN)-1
    while start<=end:
        mid=(start+end)//2
        if cardN[mid]==num:
            return print(1,end=' ')
        elif cardN[mid]<num:
            start=mid+1
        else:
            end=mid-1

    print(0,end=' ')
            


for num in numM:
    binary_search(num)