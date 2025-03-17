import math
def isitsosu (n):
    if n < 2: 
        return False
    for i in range (2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True



T=int(input())
for _ in range(T):
    n=int(input())

    a,b=n//2,n//2
    while a>0:
        if isitsosu(a) and isitsosu(b):
            print(a,b)
            break
        else:
            a -=1
            b +=1