# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    array = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    # 순서대로 0 1 2 3 4 5 6 7 8 9 * #

    left = array[10]
    right = array[11]
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = array[i]
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = array[i]
        else:
            temp_left = abs(left[1] - array[i][1]) + abs(left[0] - array[i][0])
            temp_right =abs(right[1] - array[i][1]) + abs(right[0] - array[i][0])
            
            if temp_left == temp_right:
                if hand == 'left':
                    answer += 'L'
                    left = array[i]
                else:
                    answer += 'R'
                    right = array[i]
            elif temp_left < temp_right:
                answer += 'L'
                left = array[i]
            else:
                answer += 'R'
                right = array[i]
    return answer