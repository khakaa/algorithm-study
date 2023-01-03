n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split(' '))))

# sol2.
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = tri[0][0]

for i in range(n-1):
    for j in range(len(tri[i])):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + tri[i+1][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + tri[i+1][j+1])

print(max(dp[-1]))

#  sol1.
# for i in range(1, n):
#     for j in range(len(tri[i])):
#         if i == 1:
#             tri[i][j] += tri[0][0]
#         else:
#             if j == 0:
#                 tri[i][j] += tri[i-1][0]
#             elif j == len(tri[i])-1:
#                 tri[i][j] += tri[i-1][len(tri[i-1])-1]
#             else:
#                 tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])