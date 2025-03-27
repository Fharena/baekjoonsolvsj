import sys
input=sys.stdin.readline
stack=[]
k=int(input())


for _ in range(k):
    n=int(input())
    if n==0:
        stack.pop()
        continue
    stack.append(n)

print(sum(stack))