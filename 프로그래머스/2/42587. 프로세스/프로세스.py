def solution(priorities, location):
    answer = []
    processes = [i for i in range(1, len(priorities)+1)]
    while len(processes) > 1:
        now_process = processes[0]
        now_priority = priorities[0]
        if now_priority == max(priorities):
            answer.append(now_process)
            processes = processes[1:]
            priorities = priorities[1:]
        else:
            processes = processes[1:]
            processes.append(now_process)
            priorities = priorities[1:]
            priorities.append(now_priority)
    answer.append(processes[0])
    return answer.index(location+1)+1
