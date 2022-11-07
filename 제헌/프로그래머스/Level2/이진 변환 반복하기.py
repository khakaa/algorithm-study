def solution(s):
    answer = []
    zero_count = 0
    trial = 0
    
    while True:
        if s == '1':
            break
        zero_count += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]
        trial += 1
    answer.append(trial)
    answer.append(zero_count)
    
    return answer