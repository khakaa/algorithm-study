
def solution(prices):
    answer = []
    for i in range(len(prices)):
        temp = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                temp += 1
            else:
                temp += 1
                break
        answer.append(temp)
    print(answer)
    return answer

solution([1, 2, 3, 2, 3])