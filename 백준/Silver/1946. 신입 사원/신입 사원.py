import sys
input = sys.stdin.readline


T=int(input())
for _ in range(T):

    N=int(input())
    cnt=1
    grade=[list(map(int,input().split()))for _ in range(N)]
    grade.sort()
    min_interview = grade[0][1]

    for i in range(1, N):
        if grade[i][1] < min_interview:
            cnt += 1
            min_interview = grade[i][1]
    print(cnt)