def solution(s):
    answers=[]
    if len(s)==1:
        return 1
    for i in range(1,len(s)):
        answer = ''
        count = 1
        for j in range(i,len(s),i):
            if s[j-i:j]==s[j:j+i]:
                count+=1
            else:
                if count==1:
                    answer+=s[j-i:j]
                else:
                    answer+=str(count)+s[j-i:j]
                    count=1
        if len(s[j:j+i])==i:
            if count==1:
                answer+=s[j-i:j]
            else:
                answer+=str(count)+s[j-i:j]
                count=1
        else:
            answer+=s[j:j+i]
        answers.append(len(answer))
    return min(answers)