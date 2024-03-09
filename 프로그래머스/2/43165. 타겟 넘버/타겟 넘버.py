count = 0
def dfs(num, now_sum, numbers, target, now_num):
    global count
    num += 1
    now_sum += now_num
    if num == len(numbers):
        if now_sum == target:
            count += 1
    else:
        dfs(num, now_sum, numbers, target, numbers[num])
        dfs(num, now_sum, numbers, target, -numbers[num])
def solution(numbers, target):
    a = dfs(0, 0, numbers, target, numbers[0])
    b = dfs(0, 0, numbers, target, -numbers[0])
    return count