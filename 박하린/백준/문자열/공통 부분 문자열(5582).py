f = input()
s = input()
print(len(f),len(s))
dp = [[0 for _ in range(len(s)+1)] for _ in range(len(f)+1)]

for i in range(1,len(f)+1):
    for j in range(1, len(s)+1):
        if f[i-1] == s[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp)))
