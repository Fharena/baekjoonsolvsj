w, h = map(int, input().split())  # 종이 크기 입력
cut = int(input())  # 자르는 횟수 입력

cutx = []  # 세로로 자르는 위치
cuty = []  # 가로로 자르는 위치
x = []  # 세로 조각 크기 저장 리스트
y = []  # 가로 조각 크기 저장 리스트

for i in range(cut):
    a, b = map(int, input().split())
    if a == 1:
        cutx.append(b)
    else:
        cuty.append(b)

# 정렬
cutx.sort()
cuty.sort()

# ✅ 빈 리스트 예외 처리
if cutx:
    x.append(cutx[0])  # 첫 번째 자른 부분 크기 추가
if cuty:
    y.append(cuty[0])

# ✅ 자른 부분 간 차이를 리스트에 추가
for i in range(len(cutx) - 1):
    x.append(cutx[i + 1] - cutx[i])
for i in range(len(cuty) - 1):
    y.append(cuty[i + 1] - cuty[i])

# ✅ 마지막 조각 크기 추가 (리스트가 비어 있을 경우 대비)
x.append(w - cutx[-1] if cutx else w)
y.append(h - cuty[-1] if cuty else h)

# 모든 조각의 넓이를 구한 후 최댓값 찾기
multlist = [xi * yi for xi in x for yi in y]
print(max(multlist))