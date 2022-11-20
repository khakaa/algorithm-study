T = int(input())
tc = []
for _ in range(T):
    tc.append(int(input()))
ans = []

for tc in tc:
    two_cnt = 0
    three_cnt = 0
    five_cnt = 0
    seven_cnt = 0
    eleven_cnt = 0
    
    while tc % 2 == 0:
        tc /= 2
        two_cnt += 1

    while tc % 3 == 0:
        tc /= 3
        three_cnt += 1

    while tc % 5 == 0:
        tc /= 5
        five_cnt += 1

    while tc % 7 == 0:
        tc /= 7
        seven_cnt += 1

    while tc % 11 == 0:
        tc /= 11
        eleven_cnt += 1
    ans.append(f'{two_cnt} {three_cnt} {five_cnt} {seven_cnt} {eleven_cnt}')

for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')
    