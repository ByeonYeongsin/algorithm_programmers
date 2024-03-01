def solution(s):
    temp = [s[0]]
    for i in s[1:]:
        if (len(temp)) > 0 and (i == temp[-1]):
            temp.pop()
        else:
            temp.append(i)
    if len(temp) == 0: return 1
    else: return 0