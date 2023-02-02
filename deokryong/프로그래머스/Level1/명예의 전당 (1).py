def solution(k, score):
    answer = []
    honor_list = []
    for i in range(len(score)):
        if len(answer) < k:
            honor_list.append(score[i])
        else:
            if honor_list[0] < score[i]:
                honor_list.pop(0)
                honor_list.append(score[i])
        honor_list.sort()
        answer.append(honor_list[0])
    return answer

# solution(3,[10, 100, 20, 150, 1, 100, 200])
solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	)
