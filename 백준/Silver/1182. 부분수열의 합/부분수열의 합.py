N,S=map(int,input().split())
line=list(map(int,input().split()))
cnt=0

def dfs(dep,start,n,nline):#n개 받아서 랜덤으로 넣기
    global cnt
    if dep==n:
        if sum(nline)==S:
            cnt+=1
        return

    for i in range(start,N):##중복없이 넣어야댐,넣을수 있는원소의 개수 N개
        nline[dep]=line[i]
        dfs(dep + 1, i + 1, n, nline)


for n in range(1,N+1):#원소 n개 인 부분수열
    nline=[0]*n
    dfs(0, 0, n, nline)
print(cnt)