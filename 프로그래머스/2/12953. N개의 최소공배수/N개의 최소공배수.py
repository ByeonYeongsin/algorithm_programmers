def solution(arr):
    arr.sort()
    now_num = 0
    i = 1
    while True:
        now_num = arr[-1]*i
        for j in range(0, len(arr)):
            if now_num % arr[j] != 0:
                break
        else:
            break
        i += 1
    return now_num