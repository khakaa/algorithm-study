# n = int(input())
# print('CY') if n % 2 == 0 else print('SK')

n = int(input())
my_dp = [1] * 1002
my_dp[2], my_dp[4] = 0, 0
for i in range(5, 1002):
    if i % 2 == 0:
        my_dp[i] = 0

print('SK') if my_dp[n] == 1 else print('CY')
