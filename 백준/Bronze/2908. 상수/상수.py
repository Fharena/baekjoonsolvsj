A,B=input().split()

def revers(N):
    reversstr=""
    for i in range(len(N)):
        reversstr+=N[(len(N)-1)-i]
    return int(reversstr)

if revers(A) > revers(B):
    print(revers(A))

else:
    print(revers(B))

