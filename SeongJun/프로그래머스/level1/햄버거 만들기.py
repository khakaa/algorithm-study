def solution(ingredient):
    burger = []
    answer = 0
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4):
                burger.pop()
    return answer