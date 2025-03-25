N,K=map(int,input().split())
nums=list(input())
k = K
stack=[]

for num in nums:

    while K>0 and stack and stack[-1]<num :
        stack.pop()
        K-=1

    stack.append(num) 

# if K>0:
#     for i in range(K):
#         stack.pop()
# print(*stack,sep='')
#K를 따로 보관하면 위 과정 안거쳐도 됨.
print(''.join(stack[:N-k]))







