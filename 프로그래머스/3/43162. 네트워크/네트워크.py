visited = []

def dfs(i, computers):
    global visited
    visited[i] = 1
    checks = computers[i]
    for j in range(len(checks)):
        if computers[i][j] == 1 and visited[j] == 0:
            dfs(j, computers)
            
    
def solution(n, computers):
    answer = 0
    global visited
    visited = [0] * n
    while sum(visited) != len(visited):
        for i in range(n):
            if visited[i] != 1:
                dfs(i, computers)
                answer += 1
    
    return answer