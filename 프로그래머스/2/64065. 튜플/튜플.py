def solution(s):
    answer = []
    s_list = []
    s = s[:-2].replace('{', '')
    s = s.split('}')
    for i in range(len(s)):
        if s[i][0] == ',':
            s[i] = s[i][1:]
        s[i] = s[i].split(',')
            
    # print(s)
    for i in range(1, len(s)+1):
        for ss in s:
            if len(ss) == i:
                now_s = ss
                for ans in answer:
                    now_s.remove(ans)
                answer.append(now_s[0])
                break
    for i in range(len(answer)): answer[i] = int(answer[i])
    return answer