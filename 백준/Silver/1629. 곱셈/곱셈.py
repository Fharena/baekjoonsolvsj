import sys

input=sys.stdin.readline
a,b,c= map(int,input().split())

def mult(a,b):
    if b==1:
        return a%c
    else:
        tmp = mult(a,b//2)
        if b %2 ==0:
            return (tmp * tmp) % c
        else:
            return (tmp  * tmp *a) %c
        
print(mult(a,b))

# 지수 법칙
# A^m+n = A^m x A^n

# 나머지 분배 법칙
# (AxB)%C = (A%C) *(B%C) % C