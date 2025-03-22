import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Trees = list(map(int, input().split()))

low = 0
high = max(Trees)
result = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(tree - mid for tree in Trees if tree > mid)

    if total >= M:
        result = mid  # 조건 만족하므로 더 높일 수 있음
        low = mid + 1
    else:
        high = mid - 1

print(result)
