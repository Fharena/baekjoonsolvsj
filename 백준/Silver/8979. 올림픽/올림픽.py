import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# N은 국가, K는 등수 알고싶은 국가

medals=[]
for _ in range(N):
    medals.append(list(map(int, input().split())))
    
medals.sort(key = lambda x: (x[1],x[2],x[3]), reverse=True)
target_index = [medals[i][0] for i in range(N)].index(K)
for i in range(N):
    if medals[target_index][1:] == medals[i][1:]:
        print(i + 1)
        break