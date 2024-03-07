def solution(clothes):
    dic = {}
    for a, b in clothes:
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    answer = 1
    for d in dic: 
        answer *= (len(dic[d]) +1)
    return answer-1