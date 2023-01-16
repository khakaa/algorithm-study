def solution(s):          
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=lambda x : len(x))

    for i in range(len(s)):
        s[i] = list(map(int,s[i].split(',')))

    for i in range(len(s)):
        for k in range(len(s[i])):
            if s[i][k] not in answer:
                answer.append(s[i][k])
    print(s)
    print(answer)
    # def get_num(idx1,idx2):
    #     temp = ''
    #     while True:
    #         if s[idx1][idx2] == ',':
    #             break
    #         temp += s[idx1][idx2]
    #         idx2 += 1
    #     if int(temp) not in answer:
    #         answer.append(int(temp))
    
    # for i in range(len(s)):
    #     for j in range(len(s[i])):
    #         if int(s[i][j]) in [1,2,3,4,5,6,7,8,9]:
    #             get_num(i,j)

    
    # while True:
    #     if i == len(s):
    #         break
    #     if s[i] in num_list:
    #         i = get_num(i)
    #         continue
    #     i+=1

    # print(answer)
  
    return answer
# def solution(s):
#     answer = set()
#     result = []
#     srcs = s[2:-2].split('},{')
#     srcs.sort(key=lambda x : len(x))
#     print(srcs)
#     for src in srcs:
#         temp = set(list(map(int, src.split(','))))
#         result = result + list(set.difference(temp, answer))
#         answer=temp
#     print(result)
#     return result
solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
