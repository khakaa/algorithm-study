N = int(input())
dp = [0 for _ in range(N+1)]
card = [0] + list(map(int, input().split(' '))) # 배열끼리 + 하면 합쳐진다.

# dp배열에 결과값 누적하면서 모든 경우의 수 살펴본다
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + card[j])
print(dp[N])
