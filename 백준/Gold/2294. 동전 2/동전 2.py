import sys
input = sys.stdin.readline

n, k = map(int, input().split())

list =[]

for i in range(n):
   list.append(int(input().strip()))

dp = [10001] * (k+1)#최대가 10000
dp[0] = 0

for num in list:#1,5,12
   for i in range(num, k+1):
       dp[i] = min(dp[i],dp[i-num]+1)#1원짜리 동전만 썼을경우부터 k까지의 동전개수를 계속 최소로 초기화
if dp[k] == 10001:
   print(-1)
else:
   print(dp[k])