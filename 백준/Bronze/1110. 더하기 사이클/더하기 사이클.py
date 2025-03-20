
N = input()
if len(N) == 1:
    line = [0, int(N)]
else:
    line = list(map(int, str(N))) 
origin = line
cnt = 0

def cycle(line):
    global cnt
    if cnt > 0 and line == origin:  # 처음 값과 동일하면 종료
        print(cnt)
        return    

    cnt += 1
    sum = line[0] + line[1]  # 두 자리 숫자의 합
    sumline = list(map(int, str(sum)))  
    newline = [line[1], sumline[-1]]

    cycle(newline)

cycle(line)