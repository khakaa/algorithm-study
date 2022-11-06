T = int(input())

for i in range(1,T+1):
    T_C = int(input())
    dist = 0
    now_speed = 0
    for j in range(T_C):
        N = input()
        if N[0] == '1':
            now_speed += int(N[2:])
            dist += now_speed  
        elif N[0] == '2':
            now_speed -= int(N[2:])
            if now_speed < 0:
                now_speed = 0
            dist += now_speed
        else:
            dist += now_speed
    print(f'#{i} {dist}')

