def solution(s):
    answer = True
    if s[0] !='(' or s[-1] !=')':
        return False
    elif s.count('(') != s.count(')'):
        return False
    else:
        count = 0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            else:
                count-=1
                if count<0:
                    return False
    return True