def ZS(N,x,y):##x는 시작행,
    
    global cnt

    if x>r or y>c or x+N <= r or y+N <= c: 
          ##구역에 해당 좌표가 없을때 변의길이 ^2로 그 칸을 다 지나간 경우 카운트
        cnt += N**2
        return

    if N>2:
        N//=2
        ZS(N,x,y)
        ZS(N,x,y+N)
        ZS(N,x+N,y)
        ZS(N,x+N,y+N)
    else:
        if x==r and y==c:
            print(cnt)
        elif x==r and y+1==c:
            print(cnt+1)
        elif x+1==r and y==c:
            print(cnt+2)
        elif x+1==r and y+1==c:
            print(cnt+3)



    ##카운트로 세기


n,r,c=map(int,input().split())
cnt=0
ZS(2**n,0,0)