import sys
input = sys.stdin.readline
# import sys 를 통해 input 변수에 sys.stdin.readline을 넣어줌으로써
# 평소 쓰던대로 input을 사용하여 시간을 줄일 수 있음.
N,M = map(int,input().split())

arr = list()
pre_fix_sum = [[0 for col in range(N+1)] for row in range(N+1)]
sum = 0
for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(1,N+1):
        sum += arr[i][j-1]
        pre_fix_sum[i+1][j] = sum
    sum=0

for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = 0
    for j in range(x1,x2+1):
        result += pre_fix_sum[j][y2]-pre_fix_sum[j][y1-1]
    print(result)





# array = list(map(int,input().split()))
# pre_fix_sum = [0]*100001

# sum = 0
# for i in range(1,len(array)+1):
#     sum += array[i-1]
#     pre_fix_sum[i] = sum

# M = int(input())
# for i in range(M):
#     j,k = map(int,input().split())
#     print(pre_fix_sum[k]-pre_fix_sum[j-1])