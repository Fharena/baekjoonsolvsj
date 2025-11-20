import sys
input = sys.stdin.readline

n,m = map(int, input().split())

lst = []

for i in range(1, m+1):
    for j in range(i):
        lst.append(i)

print(sum(lst[n-1:m]))
    
