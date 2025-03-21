import sys

def findnum(A, n):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == n:
            print(1)
            return
        elif A[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    print(0)

# 입력 전체를 한 번에 읽어오기
input = sys.stdin.read().split()

N = int(input[0])
A = list(map(int, input[1:N+1]))
MN = int(input[N+1])
M = list(map(int, input[N+2:]))

A.sort()

for num in M:
    findnum(A, num)
