def calculate_dp(i):
    while i % 2 == 0:
        i = i / 2
    if i == 1:
        return 1
    # if i % 2 == 0:
    #     return calculate_dp(i//2)
    return calculate_dp(i-1)+1

def solution(n):
    while n % 2 == 0:
        n = n / 2
        
    return calculate_dp(n)