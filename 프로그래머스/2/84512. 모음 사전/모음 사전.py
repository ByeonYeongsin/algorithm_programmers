import itertools
def solution(word):
    answers = []
    al = []
    for i in range(1, 6):
        answers.append([s for s in list(itertools.product('AEIOU', repeat=i))])
    for answer in answers:
        for i in answer:
            st = ''
            for j in i:
                st += j
            al.append(st)
    al.sort()
    return al.index(word)+1