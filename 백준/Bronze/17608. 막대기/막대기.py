import sys
input=sys.stdin.readline
stack=[]
n=int(input())
cnt=0
prev=0
for _ in range(n):
    stack.append(int(input()))

for _ in range(n):
    poped=stack.pop()
    if prev<poped:
        prev=poped
        cnt+=1

print(cnt)