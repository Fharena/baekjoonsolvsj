C=int(input())
for _ in range(C):
    result=list(map(int,(input().split())))
    total=0
    for i in range(1,result[0]+1):
        total += result[i]
    avg=total/result[0]
    stdentnum=0
    for i in range(1,result[0]+1):
        if result[i] > avg:
            stdentnum+=1
    
    print(format(stdentnum/result[0]*100,".3f"),"%",sep="")
