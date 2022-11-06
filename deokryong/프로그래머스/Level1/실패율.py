#실패율

def solution(N, stages):
    answer = []
    stages.sort()
    temp =[]
    for i in range(1,N+1):
        count_fail = 0
        count_reach = 0
        for j in stages:
            if i <= j:
                count_reach+=1
                if i >= j:
                    count_fail+=1
        if count_reach == 0:
            fail_rate = 0
        else:
            fail_rate = count_fail/count_reach
        temp.append([i,fail_rate])
    temp.sort(key=lambda x : (-x[1],x[0]))
    for i in range(len(temp)):
        answer.append(temp[i][0])
    return answer