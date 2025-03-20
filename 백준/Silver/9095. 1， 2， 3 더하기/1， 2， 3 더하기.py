f=[1,2,4]

def plus(n):

    if n>3:
        for i in range(3,n+1):
            f.append(f[i-1] + f[i-2] + f[i-3])

plus(11)
T=int(input())
for _ in range(T):
    print(f[int(input())-1])
