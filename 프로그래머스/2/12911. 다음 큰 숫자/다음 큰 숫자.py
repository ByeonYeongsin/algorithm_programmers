def solution(n):
    one_nums = bin(n).count('1')
    n += 1
    while True:
        if one_nums == bin(n).count('1'):
            break
        n += 1
    return n