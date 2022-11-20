def solution(participant, completion):
    # participant.sort()
    # completion.sort()
    # for i in range(len(participant)): # 전체집합 안에서
    #     if(participant[i]!=completion[i]): #전체집합의 중복 원소 개수 > 완주집합의 중복 원소 개수 이면 해당원소 리턴
    #         return participant[i]
    # return partcipant[-1]

    # 해시 사용
    hashDict= {}
    sumHash = 0
    for part in participant:
        hashDict[hash(part)]=part
        sumHash +=hash(part)
    for comp in completion:
        sumHash -= hash(comp)
    return hashDict[sumHash]