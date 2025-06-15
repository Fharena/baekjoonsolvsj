import sys
import math
input = sys.stdin.readline

a = int(input())

for i in range(2,int(math.sqrt(a))+1):
    while a%i == 0:
        print(i)
        a//=i
if a >1:
    print(a)