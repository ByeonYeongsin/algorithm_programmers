def solution(elements):
    answers = []
    for i in range(1, len(elements)+1):
        for j in range(0, len(elements)):
            if j+i < len(elements):
                answers.append(sum(elements[j:j+i]))
            else:
                answers.append(sum(elements[j:])+sum(elements[:j+i-len(elements)]))
    return len(list(set(answers)))