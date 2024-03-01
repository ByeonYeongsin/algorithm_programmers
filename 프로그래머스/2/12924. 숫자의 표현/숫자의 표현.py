def solution(n):
    answer = 0
    for i in range(1, n+1):
        nn = 0
        for j in range(i, n+1):
            nn += j
            if nn > n:
                break
            elif nn == n:
                answer += 1
                break
                
    return answer