# 콜라츠 추측

def solution(num):
    count = 0
    while num != 1:
        if count == 500:
            count = -1
            break
        if num % 2 == 0:
            num /= 2
#            print(num, end=" ")
            count += 1
        else:
            num = num * 3 + 1
            count += 1
#            print(num, end=" ")
    return count