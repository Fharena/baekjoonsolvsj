import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    stack=[]
    PS=input()
    for j in PS:
        if j=='(':
            stack.append(j)
        elif j==')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")