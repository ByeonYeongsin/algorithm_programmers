answer = 0
def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer

def change(fr, to):
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:
            return True
    return False

def dfs(begin, target, d, words):
    global answer
    # print(begin)
    # print(words)
    if begin == target:
        # print(d)
        answer = d
        return
    else:
        if len(words) == 0:
            return 
        for w in range(len(words)):
            if change(begin, words[w]):
                word = words[:w]+words[w+1:]
                dfs(words[w], target, d+1, word)