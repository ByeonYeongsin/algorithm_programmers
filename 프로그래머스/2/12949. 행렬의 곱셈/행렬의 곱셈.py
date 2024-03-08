def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        now_ans = []
        for j in range(len(arr2[0])):
            ans = 0
            for k in range(len(arr1[i])):
                ans += (arr1[i][k] * arr2[k][j])
            now_ans.append(ans)
        answer.append(now_ans)
    return answer

