T = int(input())

for i in range(1,T+1):
    h1,m1,h2,m2 = map(int,input().split())
    hour_result = 0
    minute_result = 0
    if h1 + h2 > 12:
        hour_result = h1+h2-12
    else:
        hour_result = h1+h2
    if m1+m2>59:
        hour_result+=1
        minute_result = m1+m2 - 60
    else:
        minute_result = m1+m2
    print(f'#{i} {hour_result} {minute_result}')