def solution(want, number, discount):
    answer = 0
    for i in range(0, len(discount)-sum(number)+1):
        now_discount = discount[i:i+10]
        flag = True
        for j in range(0, len(want)):
            if flag == False: break
            for k in range(0, number[j]):
                if want[j] in now_discount:
                    now_discount.remove(want[j])
                else:
                    flag = False
                    break
        if flag == True:
            answer += 1
    return answer