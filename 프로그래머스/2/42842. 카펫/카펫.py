def solution(brown, yellow):
    factors = []
    for i in range(1, yellow+1):
        if yellow % i == 0: factors.append(i)
    while len(factors) > 0:
        if (factors[0]+factors[-1])*2+4 == brown:
            return [factors[-1]+2, factors[0]+2]
        else:
            if len(factors) > 1:
                factors = factors[1:-1]
    return -1