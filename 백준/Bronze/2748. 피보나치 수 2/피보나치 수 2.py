n = int(input())

fibo =[] 
fibo.append(0)
fibo.append(1)

for i in range(2,n+1): #리스트에 피보나치 수를 계산하여 저장
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n])