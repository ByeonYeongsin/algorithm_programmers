# answers = []
# def dfs(triangle, height, now_index, cout, next_index):
#     global answers
#     cout += triangle[height][now_index]
#     if height == len(triangle)-1:
#         answers.append(cout)
#         return
#     else:
#         dfs(triangle, height+1, now_index+next_index, cout, 0)
#         dfs(triangle, height+1, now_index+next_index, cout, 1)
# def solution(triangle):
#     dfs(triangle, 0, 0, 0, 0)
#     dfs(triangle, 0, 0, 0, 1)
#     return max(answers)

def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    for depth in range(len(triangle)):
        for index in range(len(triangle[depth])):
            if depth == 0:
                dp[depth].append(triangle[depth][index])
            else:
                if index > 0 and index < depth:
                    dp[depth].append(max(dp[depth-1][index], dp[depth-1][index-1])+triangle[depth][index])
                elif index == 0:
                    dp[depth].append(dp[depth-1][index]+triangle[depth][index])
                elif index == depth:
                    dp[depth].append(dp[depth-1][index-1]+triangle[depth][index])
                    
    # print(dp)
    return max(dp[-1])
    