import sys
input= sys.stdin.readline
H,W,N,M = map(int,input().strip().split())
if H%(N+1):
    height=H//(N+1)+1
else:
    height=H//(N+1)
    
if W%(M+1):
    width=W//(M+1)+1
else:
    width=W//(M+1)
print(height*width)