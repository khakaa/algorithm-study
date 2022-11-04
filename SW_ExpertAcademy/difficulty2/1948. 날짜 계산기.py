T = int(input())

date_dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for i in range(1,T+1):
    mon1, day1, mon2, day2 = map(int,input().split())
    if mon1 == mon2:
        result = day2 - day1
    else:
        result = date_dic[mon1] - day1
        for j in range(mon1+1,mon2,1):
            result += date_dic[j]
        result += day2
    print(f'#{i} {result+1}')
