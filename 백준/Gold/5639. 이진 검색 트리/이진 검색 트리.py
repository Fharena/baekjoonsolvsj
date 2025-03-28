import sys
sys.setrecursionlimit(10 ** 6)
node = list(map(int, sys.stdin.read().split()))



def post_order(start, end):

    # 종료조건
    if start > end:
        return

    root = node[start]
    idx= start+1
    while idx<=end and node[idx] <root:#오른쪽 트리 시작서칭
        idx+=1

    post_order(start+1,idx-1)#왼
    post_order(idx,end)#오
    print(root)#루트


post_order(0, len(node) - 1) # 처음과 끝 인덱스를 초기값으로 함수를 호출한다.