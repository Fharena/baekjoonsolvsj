def div(y, x, n): 
    color = paper[y][x] # 한칸씩 진행하다 
    for i in range(y, y+n): 
        for j in range(x, x+n): 
            if color != paper[i][j]: # 다른 색 나오면
                m = n//2
                div(y, x, m) # 색종이 분할 
                div(y, x + m, m) # 색종이 분할 
                div(y + m, x, m) # 색종이 분할
                div(y + m, x + m, m) # 색종이 분할
                return
    if color == 0: # 흰색이면
        result[0] += 1
    else : # 파란색이면
        result[1] += 1
        
import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 색종이
result = [0,0] 
div(0,0,N)
print(result[0])
print(result[1])
