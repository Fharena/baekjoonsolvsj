import sys
input = sys.stdin.readline

N = input()
A = list(map(int,input().strip().split()))
B,C = map(int, input().split())

total = 0
for a in A:
    total += 1      
    x = a - B                    
    if x > 0:                       
        total += (x + C - 1) // C 
        
print(total)