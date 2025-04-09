import sys
input=sys.stdin.readline

N,M=map(int,input().split())
stone=[int(input()) for _ in range(M)]
dp=[[10000]*(int(2*N**0.5)+2) for _ in range(N+1)]#+1까지 참조하므로 다음칸 생각해서 +1이 아닌 +2

#dp[n][v] = n번째 돌로 v의 속도로 올때의 횟수
dp[1][0]=0 #첫번째 돌에 0의 속도로 오는것은 0임. 시작지점 설정

for i in range(2,N+1):#그래프 그림 보면 2번째 행부터 시작
    for j in range(1,int(2*i**0.5)+1): #속도가 0일수는 없으니까 1번 인덱스부터 시작
        if i in stone: #i번쨰 돌이 작은돌이면 해당라인은 전부 MAX값 유지
            continue
        else:
            dp[i][j]=min(dp[i-j][j-1],dp[i-j][j],dp[i-j][j+1])+1

if min(dp[N])==10000:
    print(-1)
else:
    print(min(dp[N]))