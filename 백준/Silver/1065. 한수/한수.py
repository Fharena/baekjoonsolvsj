
def hansucheck(n): ##n은 i, int로 입력받음

    Nlist=list(map(int,str(n)))
    
    dif=Nlist[0]-Nlist[1]
    for i in range(1,len(Nlist)-1):
        if Nlist[i]-Nlist[i+1]!=dif:
            return 0
    return 1
N=int(input())
if N < 100:
    print(N)  # 1~99는 모두 한수
else:
    sum=99
    for i in range(100,N+1):
        sum+=hansucheck(i)
    print(sum)