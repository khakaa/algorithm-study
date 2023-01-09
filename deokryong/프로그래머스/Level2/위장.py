def solution(clothes):
    answer = 1                                                          
    daily_fashion = dict()                                              # 의상 종류별 개수를 세기 위한 딕셔너리 생성
    for i in range(len(clothes)):                                       
        if clothes[i][1] not in daily_fashion.keys():                   # 딕셔너리에 해당 의상 종류가 없을시 생성 후 개수 1로 초기화
            daily_fashion[clothes[i][1]] = 1
        else:                                                           # 딕셔너리에 해당 의상 종류가 있을시 +1
            daily_fashion[clothes[i][1]] += 1
    
    for i in range(len(daily_fashion)):                                 # 의상 종류만큼 반복
        answer *= daily_fashion[list(daily_fashion.keys())[i]]+1        # 의상 종류별 의상의 개수 + 1을 곱해줌(Ex - headgear종류가 green,blue,yellow 3가지일경우 green선택,blue선택,yellow선택,아무것도 선택x 총 4가지이므로) 
    answer -= 1                                                         # 모든 의상을 선택안하는 경우의 수를 빼줘야하므로
    return answer

solution([["yellow_hat", "headgear"],["yw_hat", "headgear"] ,["green_turban", "headgear"],["blue_sunglasses", "eyewear"],["blue", "eyewear"],["e", "face"],["lue", "face"],["bue", "face"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
