import sys
input=sys.stdin.readline

queue=[]
head = 0
n=int(input())
for _ in range(n):
    str=list(input().split())
    if str[0]=="push":
        queue.append(int(str[1]))
    elif str[0]=="pop":
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])
            head += 1
    elif str[0]=="size":
        print(len(queue)-head)
    elif str[0]=="empty":
        if head == len(queue):
            print(1)
        else:
            print(0)
    elif str[0]=="front":
        if head == len(queue):
            print(-1)
        else:    
            print(queue[head])
    elif str[0]=="back":
        if head == len(queue):
            print(-1)
        else:
            print(queue[-1])
