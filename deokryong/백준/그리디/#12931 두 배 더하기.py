N = int(input())

A = [0]*N
B = list(map(int,input().split()))

B.sort()
count = 0
while True:
    if A == B:
        break
    chk = True
    for i in range(len(B)):
        if B[i] % 2 != 0: 
            chk =False
            B[i] -= 1
            count+=1
            break
    if chk == True:
        count+=1
        for i in range(len(B)):
            B[i] = B[i] // 2 
print(count)