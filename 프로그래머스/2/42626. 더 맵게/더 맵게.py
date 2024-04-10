import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while scoville[0] < K:
        a = hq.heappop(scoville)
        if len(scoville) >= 1:
            b = hq.heappop(scoville)
        else:
            return -1
        hq.heappush(scoville, a+b*2)
        answer+=1
    return answer