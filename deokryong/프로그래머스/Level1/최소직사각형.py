# 최소직사각형

def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][1],sizes[i][0] = sizes[i][0],sizes[i][1]
    a = max(sizes[i][1] for i in range(len(sizes)))
    b = max(sizes[i][0] for i in range(len(sizes)))
    
    return a*b