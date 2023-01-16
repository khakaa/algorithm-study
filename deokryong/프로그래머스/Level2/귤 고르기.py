def solution(k, tangerine):
    answer = 0
    count_list = []
    
    count = 1
    tangerine.sort()
    print(tangerine)
    if len(tangerine) == 1:
        count_list.append(1)
    else:
        for i in range(1,len(tangerine)):
            if tangerine[i] == tangerine[i-1]:
                count+=1
            else:
                count_list.append(count)
                count = 1
            if i==len(tangerine)-1:
                count_list.append(count)
    count_list.sort(reverse=True)
    print(count_list)
    for i in range(len(count_list)):
        if k > count_list[i]:
            k -= count_list[i]
            answer+=1
        else:
            answer+=1
            break
    print(answer)
    return answer
# solution(6,[1, 3, 2, 5, 4, 5, 2, 3])
# solution(4,[1, 3, 2, 5, 4, 5, 2, 3])
# solution(2,[1, 1, 1, 1, 2, 2, 2, 3])
solution(1,[1])

