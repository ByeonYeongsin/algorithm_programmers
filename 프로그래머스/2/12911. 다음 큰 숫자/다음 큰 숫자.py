def solution(n):
    next_num = n+1
    n = str(bin(n))[2:]
    n_one_nums = 0
    for i in n: n_one_nums += int(i)
    while True:
        next_bin = str(bin(next_num))[2:]
        next_one_nums = 0
        for i in next_bin: next_one_nums += int(i)
        if n_one_nums == next_one_nums:
            break
        else:
            next_num = next_num + 1
    return next_num