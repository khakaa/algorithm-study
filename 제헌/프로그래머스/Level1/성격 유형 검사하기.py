def solution(survey, choices):
    answer = ''
    person_dict = { 'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0 }
    person_arr = list(person_dict)
    
    for i in range(len(survey)):
        score = choices[i] - 4
        
        if score < 0:
            person_dict[survey[i][0]] += (-1) * score
        elif score > 0:
            person_dict[survey[i][1]] += score
    
    for j in range(0, len(person_dict) - 1, 2):
        if person_dict[person_arr[j]] >= person_dict[person_arr[j+1]]:
            answer += (person_arr[j])
        else:
            answer += (person_arr[j+1])
            
    return answer