def Asum(A):
	total=0
	for i in range(len(A)-1):
		total+=abs(A[i]-A[i+1])
	return total
line=[]
sumlist=[]
N=int(input())
visited = [False] * N
A=list(map(int,input().split()))

def dfs(dep):
    if dep==N:
        sumlist.append(Asum(line))
        return

    for i in range(N):
        if visited[i]==False:
            line.append(A[i])
            visited[i]=True
            dfs(dep+1)
            line.pop()
            visited[i]=False  



dfs(0)
print(max(sumlist))
