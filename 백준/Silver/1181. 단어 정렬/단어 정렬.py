N=int(input())
wlist=[]
for i in range(N):
    wlist.append(str(input()))
wlist=list(set(wlist))
wlist=sorted(wlist,key=lambda x: (len(x),x))

for i in range(len(wlist)):
    print(wlist[i])