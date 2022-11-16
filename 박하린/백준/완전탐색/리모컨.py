N = int(input())
M = int(input())
if M != 0:
    broken_btn = input().split(' ')
else:
    broken_btn = []

# + -로 이동하는 경우
min_cnt = abs(N-100)

if N == 100:
    print(0)
else:
    for n in range(1000001):
        number = str(n)

        for i in range(len(number)):
            if number[i] in broken_btn:
                break
            elif i == len(number) - 1:
                min_cnt = min(min_cnt, abs(int(number) - N) + len(number))
    print(min_cnt)