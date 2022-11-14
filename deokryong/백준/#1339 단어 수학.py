N = int(input())
dic = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
arr = ['']*N
for i in range(N):
    arr[i] = input()
    temp = len(arr[i])
    for j in range(len(arr[i])):
        dic[arr[i][j]] += 10**(temp-1)
        temp-=1
answer = sorted(dic.values(),reverse=True)
total = 0
num = 9
for i in range(len(answer)):
    if answer[i] == 0:
        break
    total += answer[i] * num
    num -= 1
print(total)