def solution(n, t, m, p):
    num = t*m
    num_str = '0'
    for i in range(0, num+1):
        now_num = i
        now_s = ''
        while now_num > 0:
            if t < 10:
                now_s = str(now_num % n) + now_s
            else:
                s = now_num%n
                if s > 9:
                    s = chr(s+ord('A')-10)
                now_s = str(s) + now_s
            now_num = now_num // n
        num_str += now_s
    # print(num_str)
    answer = ''
    for i in range(p-1, m*t, m):
        answer += num_str[i]
    return answer