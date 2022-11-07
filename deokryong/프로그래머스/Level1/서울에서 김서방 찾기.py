# 서울에서 김서방 찾기

def solution(seoul):
    answer = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = i
            break
    return f"김서방은 {i}에 있다"