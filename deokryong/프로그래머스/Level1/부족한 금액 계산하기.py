# 부족한 금액 계산하기

def solution(price, money, count):
    temp = 0
    for i in range(1,count+1):
        temp += price*i
    if money < temp:
        answer = temp - money
    else:
        answer = 0

    return answer
