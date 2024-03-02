def solution(n, words):
    spoken = []
    term = 1
    person = 1
    for word in words:
        if word in spoken:
            return [person, term]
        elif (len(spoken) > 0) and (word[0] != spoken[-1][-1]):
            return [person, term]
        else:
            spoken.append(word)
            person += 1
            if person > n:
                person -= n
                term += 1
    return [0, 0]