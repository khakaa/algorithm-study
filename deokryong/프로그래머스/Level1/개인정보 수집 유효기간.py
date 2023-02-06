def solution(today, terms, privacies):
    answer = []
    terms_dic = dict()
    for i in range(len(terms)):
        terms_dic[terms[i][0]] = int(terms[i][2:])
        
    for i in range(len(privacies)):
        year = (int(today[:4]) - int(privacies[i][:4]))*12
        month = (int(today[5:7]) - int(privacies[i][5:7]))
        day = int(today[8:10]) - int(privacies[i][8:10])
        term = terms_dic[privacies[i][-1]] * 28
        if (year + month) * 28 + day >= term:
            answer.append(i+1)
    return answer

solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
