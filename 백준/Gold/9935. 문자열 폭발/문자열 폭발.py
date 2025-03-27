import sys
input=sys.stdin.readline


stack=[]
str1=input().strip()
bombstr=input().strip()
for i in range(len(str1)):
    stack.append(str1[i])
    if len(stack) >= len(bombstr) and ''.join(stack[-len(bombstr):]) == bombstr:
        for _ in range(len(bombstr)):
            stack.pop()
result=''.join(stack)
if not stack:
    print("FRULA")
else:
    print(result)
