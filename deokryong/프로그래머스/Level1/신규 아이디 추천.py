def solution(new_id):
    answer = ''
    #1단계
    temp = ''
    step1 = False
    for i in range(len(new_id)):
        if new_id[i].isupper():
            temp += new_id[i].lower()
        else:
            temp += new_id[i]
    step1 = True
    #print(f'1단계 : {temp}')
    #2단계
    if step1 == True:
        answer = temp
        temp = ''
    step2 = False
    for i in range(len(answer)):
        if (answer[i].islower() == True) or (answer[i].isdecimal() == True) or (answer[i] == '-') or (answer[i] == '_') or (answer[i] == '.'):
            temp += answer[i]
    step2 = True
    #print(f'2단계 : {temp}')
    #3단계
    if step2 == True:
        answer = temp
        temp = ''
    step3 = False
    for i in range(len(answer)):
        if answer[i] == '.' and len(answer) > i+1:
            if answer[i+1] == '.':
                pass
            else:
                temp += answer[i]
        else:
            temp += answer[i]
    step3 = True
    #print(f'3단계 : {temp}')
    #4단계
    if step3 == True:
        answer = temp
        temp = ''
    step4 = False
    for i in range(len(answer)):
        if i == 0 and answer[i] == '.':
            answer = answer[1:]
        if i == len(answer)-1 and answer[i] == '.':
            answer = answer[:len(answer)-1]
    step4 = True
    temp = answer
                
    #print(f'4단계 : {answer}')
    #5단계
    if step4 == True:
        answer = temp
        temp = ''
    step5 = False
    if len(answer) == 0:
        temp += 'a'
        step5 = True
    #print(f'5단계 : {temp}')
    #6단계
    if step5 == True:
        answer = temp
        temp = ''
    step6 = False
    if len(answer) >= 16:
        temp = answer[:15]
        step6 = True
        if temp[-1] == '.':
            temp = temp[:len(temp)-1]
    #print(f'6단계 : {temp}')
    #7단계
    if step6 == True:
        answer = temp
        temp = ''
    while len(answer) <= 2:
        temp = answer[len(answer)-1]
        answer += temp
        
    #print(f'7단계 : {temp}')
    return answer