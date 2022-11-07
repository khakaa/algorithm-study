def solution(s):
    answer = []
    
    s = s[:-2].replace('{','').replace(',',' ').split('}')

    s = [i.split() for i in s]
    s.sort(key = lambda x : len(x))
    
    for data in s:
        res = set(data) - set(answer)
        answer.append(list(res)[0])
        
    answer = [int(i) for i in answer]
    return answer