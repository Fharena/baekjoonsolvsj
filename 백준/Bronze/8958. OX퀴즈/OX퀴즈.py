N=int(input())

OXstrgroup=[]

for i in range(N):
    OXstrgroup.append(input())

for i in range(len(OXstrgroup)):
    Ocheck = OXstrgroup[i].split("X")
    score = 0
    for j in range(len(Ocheck)):
        Oplus =1
        for k in range(len(Ocheck[j])):
            
            score+=Oplus
            Oplus+=1
    print(score)  
    
