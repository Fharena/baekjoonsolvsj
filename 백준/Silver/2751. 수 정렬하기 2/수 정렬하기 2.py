##병합정렬
def merge(arr1, arr2):
    res = []
    index1 = index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            res.append(arr1[index1])
            index1 += 1
        else:
            res.append(arr2[index2])
            index2 += 1
    if index1 == len(arr1):
        res += arr2[index2:]
    else:
        res += arr1[index1:]
    return res


def merge_sort(arr):
    if len(arr) == 1:
        return arr                # 배열의 원소가 한 개이면, 정렬된 배열이므로 그대로 반환한다.
    mid = len(arr) // 2           # 배열의 길이를 이용하여 가운데 인덱스를 계산한다.
    left = merge_sort(arr[:mid])  # 인덱스 0 ~ 인덱스 (mid-1)까지의 원소를 합병 정렬한다.
    right = merge_sort(arr[mid:]) # 인덱스 mid ~ 마지막 인덱스까지의 원소를 합병 정렬한다.
    return merge(left, right)     # 정렬한 두 배열을 합병한다.

N=int(input())
list=[]
for i in range(N):
    list.append(int(input()))


for i in merge_sort(list):
    print(i)