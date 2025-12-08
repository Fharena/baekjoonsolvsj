import sys
input = sys.stdin.readline
M = int(input())
s=set()
for _ in range(M):
    REQ = input().split()
    
    if len(REQ) ==1:
        if REQ[0]=="all":
            s = set([i for i in range(1,21)])
        else:
            s= set()
            
    else:
        com, x = REQ[0], REQ[1]
        x = int(x)
        
        if com == "add":
            s.add(x)
        elif com == "remove":
            s.discard(x)
        elif com == "check":
            print(1 if x in s else 0)
        elif com == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)