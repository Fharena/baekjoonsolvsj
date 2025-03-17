N=int(input())

def hanoi(n,frompo,topo,auxpo):#1,3,2
    if n==1:
        print(frompo,topo)##  1 3
        return 0
    hanoi(n-1,frompo,auxpo,topo)##from 에서 보조 기둥으로  n-1개 옮김
    print(frompo,topo) 

    hanoi(n-1,auxpo,topo,frompo)##보조기둥 에서 to 기둥으로  n-1개 옮김

print(2**N-1)
if N<=20:
    hanoi(N,1,3,2)
