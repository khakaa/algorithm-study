def solution(babbling):
    answer = 0
    
    def possible_chk(s):
        i = 0
        chk = True
        aya_chk = 0
        ye_chk = 0
        woo_chk = 0
        ma_chk = 0

        while True:
            if i == len(s):
                break
            if s[i] == 'a':
                if s[i:i+3] == 'aya' and aya_chk == 0:
                    i = i+3
                    aya_chk += 1
                    ye_chk = 0
                    woo_chk = 0
                    ma_chk = 0
                    continue
                else:
                    chk = False
                    break
            elif s[i] == 'y':
                if s[i:i+2] == 'ye' and ye_chk == 0:
                    i = i+2
                    ye_chk += 1
                    aya_chk = 0
                    woo_chk = 0
                    ma_chk = 0
                    continue
                else:
                    chk = False
                    break
            elif s[i] == 'w':
                if s[i:i+3] == 'woo' and woo_chk == 0:
                    i = i+3
                    woo_chk += 1
                    ye_chk = 0
                    aya_chk = 0
                    ma_chk = 0
                    continue
                else:
                    chk = False
                    break
            elif s[i] == 'm':
                if s[i:i+2] == 'ma' and ma_chk == 0:
                    i = i+2
                    ma_chk += 1
                    aya_chk = 0
                    ye_chk = 0
                    woo_chk = 0
                    continue
                else:
                    chk = False
                    break
            else:
                chk = False
                break
        # print(chk)
        return chk

    for i in range(len(babbling)):
        if possible_chk(babbling[i]):
            answer += 1
    # print(answer)
    return answer

# solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
