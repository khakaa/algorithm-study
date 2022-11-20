def cal_date(fir_m,fir_d,sec_m,sec_d):
    result = 0
    month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    if fir_m == sec_m:
        return sec_d - fir_d + 1
    else:
        for m in range(fir_m,sec_m+1):
            if m == fir_m:
                result += month[m] - fir_d
            elif m > fir_m and m < sec_m:
                result += month[m]
            else:
                result += sec_d + 1
    return result

t = int(input())
ans = []
for _ in range(t):
    fir_m,fir_d,sec_m,sec_d = map(int, input().strip().split())
    ans.append(cal_date(fir_m,fir_d,sec_m,sec_d))

for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')