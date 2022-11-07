# 크레인 인형뽑기 게임

def solution(board, moves):
    stack = list()
    answer = 0
    for i in range(len(moves)):
        if len(stack) > 1:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                stack.pop()
                answer += 2
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                stack.append(board[j][moves[i]-1])    
                board[j][moves[i]-1] = 0
                break
    return answer
