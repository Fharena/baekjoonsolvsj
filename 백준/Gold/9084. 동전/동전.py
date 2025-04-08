import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())


    d = [0] * (m + 1)
    d[0] = 1


    for coin in coins:
        for i in range(m + 1):
            if i >= coin:
                d[i] += d[i - coin] #d[i]는 coin 안쓰는 경우 d[i - coin]는 해당 코인 최소 하나는 쓰는 경우 두개 합쳐서 d[i] 로 값변경

    print(d[m])