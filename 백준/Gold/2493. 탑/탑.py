import sys
input=sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0] * N #기본은 신호 받는 스틱 없는 0


for i in range(N):#앞에서부터 검사하되 스택에는 검사하는 스틱보다 작은게 앞에있으면 전부 pop, 보다 크면 해당 스틱  인덱스+1
    while stack:
        if stack[-1][1]>towers[i]:#마지막 스택의 높이가 크면 수신\
            ans[i] = stack[-1][0] + 1 #i번째 기둥의 신호를 받는건 해당 스택의 인덱스 +1
            break
        else:
            stack.pop()


    stack.append((i,towers[i]))
print(*ans)