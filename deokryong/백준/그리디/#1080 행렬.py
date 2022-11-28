N, M = map(int,input().split())

A = []
for i in range(N):
    A.append(list(map(int,input())))

B = []
for i in range(N):
    B.append(list(map(int,input())))
    
def conversion(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            A[x][y] = 1 - A[x][y]
 

count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            conversion(i,j)
            count+=1
print(A)
print(B)

if A == B:
    print(count)
else:
    print(-1)
