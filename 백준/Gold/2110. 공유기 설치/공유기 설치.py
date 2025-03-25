import sys
N,C=map(int,sys.stdin.readline().split())#집 개수
X = [int(sys.stdin.readline()) for _ in range(N)]
X.sort()

#적절한 거리를 찾는것이기 떄문에 이분탐색은 좌표가 아닌 거리를 찾는다.
low=1
high=X[-1]-X[0]
answer=0
#첫집을 시작으로 공유기를 깔되 최적의 거리를 찾아 해당 거리보다 크거나 같은 거리에 설치했을때 공유기 
#개수가 같거나 크면 해당 값이 처음엔 무조건 들어가고 다음 루프때 해당 값보다 더 큰 값 찾으면  answer
# 에 채워넣기.이후 더 거리 좁히기. 외의 경우에는  거리 늘려가면서 찾기 
while low<=high:
    
    cur=X[0]#어떤경우던 첫번째집은 설치
    cnt = 1 #첫집에 공유기 설치
    
    mid=(low+high)//2 #현재 사용해볼 거리 
    for i in range(1,N):
        if X[i]-cur>=mid:
            cnt+=1 #설치
            cur=X[i] #현재 집 설치한집으로 바꾸기
    if cnt>=C:
        if answer<mid:#최댓값 찾아야되니까 개수 맞는 mid가 더 크면 answer로 이동
            answer=mid
        low=mid+1
    else:
        high=mid-1


print(answer)