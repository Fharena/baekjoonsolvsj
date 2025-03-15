A=int(input())
B=int(input())
C=int(input())

tmp=str(A*B*C)
for i in range(10):
    cnt=0

    for j  in range(len(tmp)):
        
        if int(tmp[j])==i:
            cnt+=1
    
    print(cnt)