import sys

input=sys.stdin.readline

def sol(h,low,high):#이분탐색처럼 중간값으로 쪼갬
    if low==high:#한칸이라는뜻이므로 최댓값은 그 놓이
        return h[low]
    elif high-low ==1:#두칸일때
        if h[high]<h[low]:
            return max(2*h[high],h[low])
        else:
            return max(2*h[low],h[high])
    mid=(low+high)//2
    leftarea=sol(h,low,mid)
    rightarea=sol(h,mid+1,high)

    left=mid
    right=mid
    midarea = h[mid]
    nowh = h[mid]
    while low <= left and right <= high:
        midarea = max(midarea, nowh * (right - left + 1))

        # 높이가 더 높은 쪽으로 확장
        if left == low:
            right += 1
            if right > high:
                break
            nowh = min(nowh, h[right])
        elif right == high:
            left -= 1
            if left < low:
                break
            nowh = min(nowh, h[left])
        else:
            if h[left - 1] > h[right + 1]:
                left -= 1
                nowh = min(nowh, h[left])
            else:
                right += 1
                nowh = min(nowh, h[right])
    return max(leftarea,rightarea,midarea)
while True:
    h=list(map(int,input().split()))
    n=h[0]
    if n==0:
        break
    print(sol(h,1,n))


 