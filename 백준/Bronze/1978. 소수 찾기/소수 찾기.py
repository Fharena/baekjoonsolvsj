N=int(input())
Num=list(map(int,input().split()))
cnt=0

for i in range(N):
    check=0
    if Num[i]>1:
        for j in range(2,Num[i]):
            if Num[i]%j==0:
                check=1
                break
        if check==0:
            cnt+=1
        
        

print(cnt)