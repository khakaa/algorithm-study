T = int(input())

for i in range(1,T+1):
    N = int(input())
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0

    while True:
        if N % 2==0:
            count_a += 1
            N /= 2
        elif N % 3==0:
            count_b += 1
            N /= 3
        elif N % 5==0:
            count_c += 1
            N /= 5
        elif N % 7==0:
            count_d += 1
            N /= 7
        elif N % 11==0:
            count_e += 1
            N /= 11
        else:
            break
    print(f'#{i} {count_a} {count_b} {count_c} {count_d} {count_e}')
        