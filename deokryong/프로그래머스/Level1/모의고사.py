# 모의고사

def solution(answers):
    answer = [0]*3
    people_1 = [1,2,3,4,5]
    people_2 = [2,1,2,3,2,4,2,5]
    people_3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    for i in range(len(answers)):
        if answers[i] == people_1[i % 5]:
            answer[0] += 1
        if answers[i] == people_2[i % 8]:
            answer[1] += 1
        if answers[i] == people_3[i % 10]:
            answer[2] += 1
    result = []
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i+1)
    return result
