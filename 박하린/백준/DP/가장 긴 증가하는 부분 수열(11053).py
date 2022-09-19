from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp = []

for a in arr:
    p = bisect_left(dp, a)

    if len(dp) <= p:
        dp.append(a)
    else:
        dp[p] = a
    print(dp)
    
print(len(dp))