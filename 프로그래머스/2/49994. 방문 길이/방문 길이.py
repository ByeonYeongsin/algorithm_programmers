def solution(dirs):
    fl = (0, 0)
    tracks = []
    answer = 0
    for dir in dirs:
        if dir == 'U': nl = (fl[0], fl[1]+1)
        elif dir == 'D': nl = (fl[0], fl[1]-1)
        elif dir == 'R': nl = (fl[0]+1, fl[1])
        elif dir == 'L': nl = (fl[0]-1, fl[1])
        if nl[0] < -5 or nl[0] > 5 or nl[1] > 5 or nl[1] < -5:
            nl = fl
            continue
        if [fl[0], fl[1], nl[0], nl[1]] not in tracks:
            answer += 1
            tracks.append([fl[0], fl[1], nl[0], nl[1]])
            tracks.append([nl[0], nl[1], fl[0], fl[1]])
        fl = nl
        # print(fl, answer)
    return answer