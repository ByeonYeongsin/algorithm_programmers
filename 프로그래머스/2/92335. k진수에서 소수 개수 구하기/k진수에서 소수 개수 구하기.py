def solution(n, k):
    import math
    nn, answer = '', 0
    while n > 0:
        nn = str(n%k) + nn
        n = n // k
    n = str(int(nn))
    n = n.split('0')
    for now_num in n:
        if now_num != '' and now_num != '1':
            if int(now_num) == 2: answer += 1
            else:
                # for j in range(2, int(now_num)//2+1):
                for j in range(2, int(math.sqrt(int(now_num)))+1):
                    if int(now_num) % j == 0: 
                        break
                else:
                    answer += 1
    return answer