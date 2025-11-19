import sys
input = sys.stdin.readline

N , K =  map(int,input().split())
x=0
for i in range(1,N+1):
    if N%i == 0:
        x+=1
        if x==K:
            print(i)
            break
if x<K:
    print(0)
    
    