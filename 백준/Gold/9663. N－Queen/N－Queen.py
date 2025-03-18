N=int(input())

result =0

# queen_positions 리스트는 각 행에 배치한 퀸의 열 번호를 저장합니다.
# 예를 들어 queen_positions[2] = 4 라면 3번째 행(인덱스 2)에 5번째 열(인덱스 4)에 퀸이 있다는 의미입니다.

queen_positions=[-1]*N


def is_possible(row):
    for i in range(row):
        if queen_positions[row] == queen_positions[i] or abs(queen_positions[row]-queen_positions[i])== row-i:
            return False
    return True

def dfs(row):
    global result
    if row==N: #모든 행의 퀸 배치 완료시 카운트 +1
        result +=1
        return
    
    for col in range(N):
        queen_positions[row] =col ## row 행의 col 열에 배치
        if is_possible(row): ## 가능한 위치인가 확인
          dfs(row+1)##다음행으로 


# 0행부터 탐색 시작
dfs(0)
print(result)