def solution(n):
    answer = 0
    user_dp = [i for i in range(1, n+1)]
    start_idx, end_idx = 0, 0
    interval_sum = 0
    
    for i in range(n):
        print(interval_sum, answer)
        while interval_sum < n and end_idx < n:
            interval_sum += user_dp[end_idx]
            end_idx += 1
        if interval_sum == n:
            answer += 1
        interval_sum -= user_dp[i]
    
    return answer