def solution(msg):
    answer = []
    dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    
    count = 0
    idx = 27
    for i in range(len(msg)):
        if count != 0:
            count -= 1
            continue
        temp = msg[i]
        temp2 = ''
        for j in range(i+1,len(msg)):
            if temp + msg[j] not in list(dic.keys()):
                temp2 = temp+msg[j]
                break
            temp += msg[j]
            count += 1
        answer.append(dic[temp])
        print('temp',temp)
        print('temp2',temp2)
        print('answer',answer)
        dic[temp2] = idx
        idx+=1
        # print('len(dic)', len(dic.keys()))
    print(answer)
    return answer

solution("KAKAO")
solution("TOBEORNOTTOBEORTOBEORNOT")
solution("ABABABABABABABAB")

