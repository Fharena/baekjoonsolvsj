w,h=map(int,input().split())
cut=int(input())
cutpaper = []
cutx=[] ##앞 숫자가 1로 받음
cuty=[]## 앞숫자가 0으로 받아 가로커팅해야 세로 길이 나옴
x=[]
y=[]

for i in range(cut):
    a,b=map(int,input().split())
    if a==1:
        cutx.append(b)
    else:
        cuty.append(b)
##xcut,ycut에 자른 위치 다 넣음
cutx.sort()
cuty.sort()
# print(cutx)
# print(cuty)
if cutx:  #빈 리스트면 뒤에가서 전체 길이 줄거임
    x.append(cutx[0])
if cuty:
    y.append(cuty[0])

##차이 집어넣기 x,y에

for i in range(len(cutx)-1):
    x.append(cutx[i+1]-cutx[i])
x.append(w - cutx[-1] if cutx else w) #안자를때는 w 통째로 주기

for i in range(len(cuty)-1):
    y.append(cuty[i+1]-cuty[i])
y.append(h - cuty[-1] if cuty else h) #안자를때는 h 통째로 주기
# print(x)
# print(y)

multlist=[]

for i in range(len(x)):
    for j in range(len(y)):
        multlist.append(x[i]*y[j])
print(max(multlist))