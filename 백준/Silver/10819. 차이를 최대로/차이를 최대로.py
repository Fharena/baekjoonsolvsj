
# Asum[A,n]=A[n]+Asum[A,n-1]
def Asum(arr):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i + 1])
    return total

def dfs(dep):
    if dep==N:
        sumlist.append(Asum(explore))
        return
    
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            explore.append(A[i])
            dfs(dep + 1)
            explore.pop() 
            visited[i] = False


N=int(input())
sumlist=[]
explore=[]
visited = [False] * N
A=list(map(int,input().split()))
dfs(0)
print(max(sumlist))