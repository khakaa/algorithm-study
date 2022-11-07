import sys
input = sys.stdin.readline
# import sys 를 통해 input 변수에 sys.stdin.readline을 넣어줌으로써
# 평소 쓰던대로 input을 사용하여 시간을 줄일 수 있음.
N,K = map(int,input().split())
array = list(map(int,input().split()))

pre_fix_sum = [0]*(N)

for i in range(N):
    if i>K-1:
        pre_fix_sum[i] = pre_fix_sum[i-1]-array[i-K]+array[i]
    else:
        pre_fix_sum[i] = pre_fix_sum[i-1]+array[i]
for i in range(K-1):
    pre_fix_sum[i] = 0

print(max(pre_fix_sum))


