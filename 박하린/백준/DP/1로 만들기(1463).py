# @author Harin 
# @date 2022.09.06.
# 문제 링크 : https://www.acmicpc.net/problem/1463

n = int(input()) # 입력값 int로 변환
dp = [0] * (n+1) # dp 길이 n+1, 값은 0으로 초기화한 배열

# 1은 답이 0이라 2부터 반복문 시작
for i in range(2,n+1):
    dp[i] = dp[i - 1] + 1 # 일단 1을 빼면 되는 경우부터 계산

    # 3으로 나눠떨어지는 경우 현재 dp[i]와 3으로 나눈 몫의 값 + 1중 작은 값으로 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) 

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])