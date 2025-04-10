import sys
input = sys.stdin.readline

n=int(input())
dp=[50001]*(n+1)
dp[0]=0
for i in range(n+1):
    for j in (5,2):
        if i>=j:
            dp[i]=min(dp[i-j]+1,dp[i])
if dp[n]==50001:
    print(-1)
else:    
    print(dp[n])