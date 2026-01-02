import sys
input = sys.stdin.readline

N = int(input())
result=[1 for _ in range(N)]
scale = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if scale[i][0]>scale[j][0] and scale[i][1]>scale[j][1]:
            result[j] +=1
        elif scale[i][0]<scale[j][0] and scale[i][1]<scale[j][1]:
            result[i] +=1
print(*result)