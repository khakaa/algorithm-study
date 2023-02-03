def solution(number, limit, power):
    answer = 0
    divisor_list = []
    for i in range(1,number+1):
        count = 0
        j = 1
        while j*j <= i:
            if j * j == i:      # 3 * 3 == 9와 같이 약수가 한개인 경우 
                count += 1
            elif i % j == 0:    # 8 % 4 == 2와 같이 약수가 두개인 경우
                count += 2
            j+=1
        divisor_list.append(count)
        if divisor_list[i-1] > limit:
            answer += power
        else:
            answer += divisor_list[i-1]
    
    return answer

solution(5,3,2)
solution(10,3,2)
