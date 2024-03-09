def solution(operations):
    import collections
    queue = collections.deque()
    for operation in operations:
        com, num = operation.split(" ")
        if com == 'I':
            if len(queue) == 0: queue.append(int(num))
            else:  
                index = 0
                for i in range(len(queue)):
                    if queue[i] < int(num):
                        index += 1
                    else:
                        break
                queue.insert(index, int(num))
        else:
            if len(queue) > 0:
                if num == '1':
                    queue.pop()
                elif num == '-1':
                    queue.popleft()
    if not queue: return [0, 0]
    return [queue[-1], queue[0]]