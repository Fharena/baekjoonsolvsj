T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):  
    result = input()  # OX 문자열 입력
    final = 0  # 총 점수
    score = 1  # 현재 연속 O에 대한 가산점

    for j in range(len(result)):
        if result[j] == 'O':
            final += score
            score += 1  # 연속된 'O'일 때 점수 증가
        else:
            score = 1  # 'X'가 나오면 가산점 초기화


##OX 결과값을 받자마자 출력을 하는 방식이며 추가로 점수 카운트는 
##인덱스를 하나씩 뒤로 가며 o이면 1에서 1점씩 더한 수를 파이널에 저장하고
##x가 나오면 score을 1로 초기화 하며 더하지 않는 루프임
    print(final)
