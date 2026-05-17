import heapq
def solution(scoville, K):
    answer = 0
    scv = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        scv = heapq.heappop(scoville)

        if scv >=K:
            break
        else:
            scv = scv + (2*heapq.heappop(scoville))
            heapq.heappush(scoville,scv)
            answer+=1
        
    return answer