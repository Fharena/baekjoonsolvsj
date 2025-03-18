# def brutal(hlist):
#     if j==9:
#         return
#     sum=0
#     for i in range(len(hlist)):
#         sum+=hlist()
#         j+=1
#         brutal
def searchfake(hlist,fsum):
    for i in range(len(hlist)):
        for j in range(len(hlist)):
            if hlist[i]+hlist[j]==fsum and hlist[i]!=hlist[j]:
                return hlist[i]
sum=0
hlist=[]
for _ in range(9):
    hlist.append(int(input()))
for i in range(9):
    sum+=hlist[i]

fsum=sum-100

f1=searchfake(hlist,fsum)
f2=fsum-f1



hlist.remove(f1)
hlist.remove(f2)
hlist.sort()
for i in range(len(hlist)):
    print(hlist[i])

