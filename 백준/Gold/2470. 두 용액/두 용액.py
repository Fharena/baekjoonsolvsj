import sys
input=sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))
X.sort()

left = 0#low
right = n-1#right

answer = abs(X[left] + X[right])
final = [X[left], X[right]]


while left < right:
    
    sum = X[left] + X[right]
    
    if abs(sum) < answer:
        answer = abs(sum)
        final = [X[left], X[right]]
        if answer == 0:
          break
    if sum < 0:#조정
        left += 1
    else:
        right-=1

print(final[0], final[1])