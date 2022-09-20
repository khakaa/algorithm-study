st = input()

count = 0
result = ""
for i in range(len(st)):
    if st[i] == 'X':
        result += 'B'
        count+=1
        if count >= 4:
            result = result.replace('BBBB','AAAA')
            count -= 4
        if i+1 == len(st) and count % 2 == 1:
            result = '-1'
            break
    else:
        if count % 2 == 1:
            result = '-1'
            break
        result += '.'
        count= 0
print(result)

            