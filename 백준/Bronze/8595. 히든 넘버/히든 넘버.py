import sys
input = sys.stdin.readline

n = int(input())
arr = input()
sum = 0
num = ''
for i in arr:
    if '0'<= i <='9':
        num+= i 
    elif num != '':
        sum += int(num)
        num = ''
if num != '':
    sum += int(num)
    num = ''
    
print(sum)