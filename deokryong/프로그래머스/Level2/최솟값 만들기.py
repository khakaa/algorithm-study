def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[len(A)-1-i]
    return answer

#test case
# print(solution([1, 4, 2],[5, 4, 4]))
# print(solution([1, 2],[3, 4]))
