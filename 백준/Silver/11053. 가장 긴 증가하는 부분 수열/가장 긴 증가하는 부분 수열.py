import sys
input=sys.stdin.readline
def binary_search(target,lis):
    low=0
    high=len(lis)-1

    while low<high:
        mid=(low+high)//2

        if target==lis[mid]:#타겟이 lis 미드값과 같으면 바로 집어넣고
            return mid
        elif lis[mid-1]<target<lis[mid]: #mid보단 작은데 그 바로 전값보다 크면 mid 좌표에 집어넣기
            return mid
        elif target<lis[mid]: #여기서부터 위치조정 들어감,lis[mid]보다 타겟이 작을경우
            high=mid-1
        else: # lis[mid]보다 타겟이 클 경우
            low=mid+1
    return low
def sol():
    n = int(input())
    a = list(map(int,input().split()))
    lis = [a[0]] # A 수열의 첫번째 값
    # A 수열의 두번째 값부터 LIS의 마지막 값과 비교
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: # 타겟이 더 크다면 LIS 에 추가
            lis.append(target)
        else:                # 타겟이 더 작다면 이분탐색을 통해 LIS 갱신,lis의 값중 target 보다 크면서 제일 작은값으로
            x = binary_search(target,lis)
            lis[x] = target

    return len(lis) # 최종 LIS 길이 반환

print(sol())