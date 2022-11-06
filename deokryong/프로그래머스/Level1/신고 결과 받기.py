#신고 결과 받기

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_id_list = {}
    dic_count_list = {}
    array=[]
    for i in range(len(id_list)):
        dic_id_list[id_list[i]] = []
        dic_count_list[id_list[i]] = 0

    for i in range(len(report)):
        a,b = report[i].split()
        if b not in dic_id_list[a]:
            dic_id_list[a].append(b)
            dic_count_list[b] += 1
    for key,value in dic_count_list.items():
        if value >= k:
            array.append(key)
  
    for i in range(len(id_list)):
        for j in range(len(array)):
            if array[j] in dic_id_list[id_list[i]]:
                answer[i] += 1
    return answer