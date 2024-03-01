def solution(s):
    words = s.split(' ')
    answer = ''
    for word in words:
        if word.isalpha():
            answer += word.capitalize()
        else:
            answer += word.lower()
        answer += ' '
    return answer[:-1]