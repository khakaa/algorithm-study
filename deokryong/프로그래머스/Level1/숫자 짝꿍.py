# X원소를 비교하면서 count를 통해 제거하는 식으로 진행
def solution(X, Y):
    answer = ''
    best_frined = []
    X_list = list(X)
    Y_list = list(Y)
    while X:
        if len(Y) == 0:
            break
        temp = X[0]
        temp_X_count = X_list.count(temp)
        temp_Y_count = Y_list.count(temp)
        min_count = temp_X_count if temp_X_count < temp_Y_count else temp_Y_count

        for _ in range(min_count):
            best_frined.append(temp)
        X = X.replace(temp,"")
        Y = Y.replace(temp,"")

    best_frined.sort(reverse=True)
    if len(best_frined) == 0:
        answer = "-1"
    else:
        if best_frined[0] == '0':
            answer = '0'
        else:
            answer = "".join(best_frined)
    return answer

solution("100","2345")
solution("100","203045")
solution("100","123450"	)
solution("12321","42531")
solution("5525","1255")
