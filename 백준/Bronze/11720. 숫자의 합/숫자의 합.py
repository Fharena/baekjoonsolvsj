import sys
input = sys.stdin.readline

N = int(input())
a = input().strip()
sum = 0
for i in a:
    sum+=int(i)
print(sum)