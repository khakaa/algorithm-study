def solution(sizes):
    W = 0
    H = 0
    for i in range(len(sizes)):
        sizes[i].sort()
        W = max(W,sizes[i][0])
        H = max(H,sizes[i][1])
        #print(W,H)
    return W*H
print(solution)