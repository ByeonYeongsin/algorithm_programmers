def solution(s):
    answer = True
    stack = []
    for al in s:
        if al == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop()
    if len(stack) != 0: answer = False    
    return answer