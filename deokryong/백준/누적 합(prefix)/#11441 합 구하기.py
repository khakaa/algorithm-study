N = int(input())
array = list(map(int,input().split()))
pre_fix_sum = [0]*100001

sum = 0
for i in range(1,len(array)+1):
    sum += array[i-1]
    pre_fix_sum[i] = sum

M = int(input())
for i in range(M):
    j,k = map(int,input().split())
    print(pre_fix_sum[k]-pre_fix_sum[j-1])