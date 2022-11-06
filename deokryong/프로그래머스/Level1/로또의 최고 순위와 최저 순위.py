# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    count_win = 0
    count_zero = 0
   
    for lotto in lottos:
        if lotto != 0 and lotto in win_nums:
                count_win += 1
        elif lotto == 0:
            count_zero += 1
    if count_win + count_zero < 2:
        answer.append(6)
        answer.append(6)  
    else:
        answer.append(6-(count_win+count_zero)+1)
        if count_win == 0 or count_win == 1:
            answer.append(6-1+1)
        else:
            answer.append(6-count_win+1)

    return answer
