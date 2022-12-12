def solution(board, moves):
    result = []
    count = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] > 0:
                result.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break
        if len(result)>=2:
            if result[-1] == result[-2]:
                del result[-2:]
                count +=2
    return count