def solution(record):
    answer = []
    dic = dict()
    # Enter일때 dic에 userid에 해당하는 nickname 넣어주기
    # Change일때 dic에 userid에 해당하는 nickname 변경해주기
    for i in range(len(record)):
        order = record[i].split()[0]
        if order == 'Enter':
            dic[record[i].split()[1]] = record[i].split()[2]
        elif order == "Change":
            dic[record[i].split()[1]] = record[i].split()[2]

    # Enter일때와 Leave일때만 해당하는 userid의 nickname으로 명령어 수행
    for i in range(len(record)):
        order = record[i].split()[0]
        id = record[i].split()[1]
        if order == 'Enter':
            answer.append(f"{dic[id]}님이 들어왔습니다.")
        elif order == "Leave":
            answer.append(f"{dic[id]}님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])