import sys
input=sys.stdin.readline
stack=[]
N=int(input())
for _ in range(N):
    str=list(input().split())
    if str[0]=="push":
        stack.append(int(str[1]))
    elif str[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif str[0]=="size":
        print(len(stack))
    elif str[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif str[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])