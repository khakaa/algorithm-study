from collections import deque
def solution(priorities, location):
    answer = 0
    print_list = deque()
   
    for i in range(len(priorities)):
        if i == location:
            print_list.append([priorities[i],1])
        else:
            print_list.append([priorities[i],0])
    
    # print(priorities)
    # print(print_list)

    while True:
        if len(print_list) == 0 or len(priorities) == 0:
            break
        priority = print_list[0][0]
        find = print_list[0][1]
        if priority == max(priorities):
            answer+=1
            priorities.pop(0)
            if location == find:
                break
        else:
            print_list.append([priority,find])
            print_list.popleft()
            priorities.append(priorities[0])
            priorities.pop(0)
        print(priorities)
        print(print_list)
    # print(print_list)
    # print(answer)
    return answer
solution([2, 1, 3, 2],2)
solution([1, 1, 9, 1, 1, 1],0)