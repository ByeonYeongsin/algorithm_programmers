def solution(s):
    zero_nums = 0
    change_nums = 0
    while len(s) > 1:
        zero_nums += len(s)
        for i in s:
            zero_nums -= int(i)
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        change_nums += 1
    answer = [change_nums, zero_nums]
    return answer