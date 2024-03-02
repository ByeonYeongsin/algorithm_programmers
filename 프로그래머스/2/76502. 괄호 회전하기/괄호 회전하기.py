def check_stack(s):
    stack = []
    for i in s:
        if i == '(': stack.append(0)
        elif i == '[': stack.append(1)
        elif i == '{': stack.append(2)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != 0: return False
            else: stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] != 1: return False
            else: stack.pop()
        elif i == '}': 
            if len(stack) == 0 or stack[-1] != 2: return False
            else: stack.pop()
    if len(stack) == 0: return True
    else: return False
    
def solution(s):
    answer = 0
    now_s = s
    for i in range(0, len(s)):
        if i > 0:
            now_s = s[i:] + s[0:i]
        if check_stack(now_s): answer += 1
    return answer