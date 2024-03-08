def solution(str1, str2):
    str1_com = []
    str2_com = []
    for i in range(len(str1)-1):
        str1_com.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        str2_com.append(str2[i:i+2].lower())

    removes = []
    for ss in str1_com:
        if len(ss.strip(" ")) < 2:
            removes.append(ss)
        else:
            for s in ss:
                if s >= 'a' and s<= 'z': continue
                else:
                    removes.append(ss)
                    break
    for rm in removes: str1_com.remove(rm)
    
    removes = []
    for ss in str2_com:
        if len(ss.strip(" ")) < 2:
            removes.append(ss)
        else:
            for s in ss:
                if s >= 'a' and s<= 'z': continue
                else:
                    removes.append(ss)
                    break
    for rm in removes: str2_com.remove(rm)
    
    print(str1_com)
    print(str2_com)
        
    overall = str1_com.copy()
    os1 = str1_com.copy()
    for s in str2_com:
        if s in os1: 
            os1.remove(s)
        else: overall.append(s)
    overall = len(overall)
    inter = 0
    if overall == 0: return 65536

    for s in str1_com:
        # print(s, str2_com, inter)
        if s in str2_com:
            inter += 1
            str2_com.remove(s)
    # print(inter)
    
    return int((inter/overall) * 65536)

    