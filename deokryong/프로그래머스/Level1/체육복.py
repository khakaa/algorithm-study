# 체육복

def solution(n, lost, reserve):
    j = 0
    while j != len(lost):
        if lost[j] in reserve:
            temp = lost[j]
            lost.remove(temp)
            reserve.remove(temp)
        else:
            j+=1
    i=0
    lost.sort()
    reserve.sort()
    while i != len(lost):
        if lost[i]-1 in reserve:
            temp = lost[i]
            reserve.remove(temp-1)
            lost.remove(temp)
            #print(i,lost, reserve)

        elif lost[i]+1 in reserve:
            temp = lost[i]
            lost.remove(temp)
            reserve.remove(temp+1)
            #print(i,lost, reserve)
        else:
            i+=1
            #print(i)
    #print(lost)
    return n - len(lost)