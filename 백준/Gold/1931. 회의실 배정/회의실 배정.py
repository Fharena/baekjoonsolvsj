import sys
input=sys.stdin.readline

N=int(input())

time=[list(map(int,input().split()))for _ in range(N)]

time.sort(key=lambda x: (x[1], x[0]))#끝시간순 소팅,같으면 시작시간

cnt = 0
end_time = 0

for start, end in time:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)