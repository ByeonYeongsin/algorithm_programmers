def solution(progresses, speeds):
    import math
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    max_day = max(days)
    answer = []
    print(days)
    for i in range(1, max_day+1):
        count = 0
        for day in days:
            if day <= i:
                count += 1
            else:
                break
        if count != 0: answer.append(count)
        days = days[count:]
    return answer