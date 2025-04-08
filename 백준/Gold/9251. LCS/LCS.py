import sys
input = sys.stdin.readline

X=input().strip()
Y=input().strip()

dp=[[0]*(len(Y)+1)for _ in range(len(X)+1)]

for i in range(1,len(X)+1):
    for j in range(1,len(Y)+1):
        if X[i-1] == Y[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[len(X)][len(Y)])