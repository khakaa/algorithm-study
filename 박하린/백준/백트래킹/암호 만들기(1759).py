def back_tracking(cnt, idx):
    if cnt == L:
        v_cnt, c_cnt = 0,0

        for a in answer:
            if a in collection:
                c_cnt += 1
            else:
                v_cnt += 1

        if c_cnt >= 1 and v_cnt >= 2:
            print(''.join(answer))

        return 
    
    for i in range(idx, C):
        answer.append(alpha[i])
        back_tracking(cnt + 1, i + 1)
        answer.pop()

# L : 암호 자리수 , C : 주어진 알파벳 개수
L,C = map(int, input().split(' '))
alpha = sorted(list(input().split(' ')))
collection = ['a','e','i','o','u']
answer = []
back_tracking(0,0)
