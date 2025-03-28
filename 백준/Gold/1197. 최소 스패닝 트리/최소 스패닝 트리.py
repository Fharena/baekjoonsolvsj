import sys
sys.setrecursionlimit(10 ** 6)
V, E = map(int, input().split())
edges = []

for _ in range(E):
    edges.append(list(map(int, input().split())))

#union find

root= dict()
for i in range(1, V+1):#딕셔너리에 다 끊어진 상태의 노드들 구현 인덱스 값의 부모는 자기자신인 식으로
    root[i]=i

#루트노드 찾는 함수 -> 완료되면 root[x]에는 x부모가 아닌 x의루트 노드가 들어가있음
def find(x):
    if root[x]==x:#부모 없으면 자기자신 리턴
        return x
    else:
        root[x]=find(root[x])
        return root[x]

#path 연결, y의 루트노드의 부모자리에 x의 루트노드넣으면서 연결하기
def union(x,y):
    x=find(x)
    root[find(y)]=x

edges = sorted(edges, key=lambda x: x[2])#cost 오름차순으로 정렬
 
total_cost = 0
 
for edge in edges:
    if find(edge[0]) == find(edge[1]):#루트가 같다면 합쳤을때 사이클 생기므로 패스
        continue
    else:
        total_cost += edge[2]
        union(edge[0], edge[1])
 
print(total_cost)#사이클 없는 제일 짧은 경로 완성