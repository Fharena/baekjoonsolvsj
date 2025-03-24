import sys
input=sys.stdin.readline

N,B= map(int,input().split())
X=[list(map(int,input().split())) for _ in range(N)]

def multi(a,b): #행렬곱 구현
    X = [[0]*N for _ in range(N)]
    for i in range(N): # 행렬
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k]*b[k][j] %1000
    return X

def square(X,n):#제곱하시오,행렬곱은 위에 구현했음 
    if n==1:
        return X
    tmp=square(X,n//2)
    if n%2==0:#지수가 짝수면
        return multi(tmp,tmp)
    else:
        return multi(multi(tmp,tmp),X)
result= square(X,B)
for i in range(N): #요구조건 대로 1000으로 나눠주자
    for j in range(N):
        result[i][j] = result[i][j] %1000
for i in range(N):
    for j in range(N):
        print(result[i][j],end=' ')
    print()