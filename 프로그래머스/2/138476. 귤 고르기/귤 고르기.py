def solution(k, tangerine):
    dic = {}
    for t in tangerine:
        if t in dic: dic[t] += 1
        else: dic[t] = 1
    remove_num = len(tangerine) - k
    flag = True
    for i in range(1, len(tangerine)):
        if flag == False: break
        for j in dic.keys():
            if dic[j] == i:
                if remove_num >= i:
                    remove_num -= i
                    dic[j] -= i
                else:
                    remove_num = 0
                    dic[j] -= remove_num
            if remove_num == 0:
                flag = False
                break
    answer = 0
    for key in dic.keys(): 
        if dic[key] != 0:
            answer += 1
    return answer