n = int(input())

change_money = [5,2]
chk = True
count = 0 
while True:
    if n ==0:
        break
    if n % 5 == 0:
        count += (n/5)
        n=0
    elif n % 5 != 0 and n > 10:
        n -= 5
        count+=1
    elif n < 10 and n % 2 ==0:
        count += (n/2)
        n=0
    elif n < 10 and n % 2 != 0:
        n -= 5
        count += 1
    else:
        chk = False
        break

if chk == True:
    print(count)
else:
    print(-1)