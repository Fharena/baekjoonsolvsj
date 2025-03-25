import sys
input = sys.stdin.readline

n = int(input())
queue = []
head = 0  # 큐의 앞을 가리키는 인덱스

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        queue.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])
            head += 1

    elif cmd[0] == "size":
        print(len(queue) - head)

    elif cmd[0] == "empty":
        print(1 if head == len(queue) else 0)

    elif cmd[0] == "front":
        if head == len(queue):
            print(-1)
        else:
            print(queue[head])

    elif cmd[0] == "back":
        if head == len(queue):
            print(-1)
        else:
            print(queue[-1])
