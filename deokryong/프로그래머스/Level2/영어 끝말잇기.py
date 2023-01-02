def solution(n, words):
    answer = []
    chk = [words[0]]
    chk2 = False
    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in chk:
            idx1 = (i % n) + 1
            idx2 = i // n + 1

            chk2 = True
            break
        else:
            chk.append(words[i])
    if chk2 == False:
        answer = [0,0]
    else:
        answer = [idx1,idx2]
    print(answer)
    return answer
solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2,["hello", "one", "even", "never", "now", "world", "draw"])
