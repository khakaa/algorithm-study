N = int(input())
high = list(map(int, input().split(' ')))
stack = []
ans = []

# 시간초과 ㅠ
# for i in range(N-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if high[i] < high[j]:
#             ans.append(j+1)
#             break
        
#         if j == 0:
#             ans.append(0)
# ans.append(0)
# ans = list(map(str, ans[::-1]))


for i in range(N):
    while stack:
        if stack[-1][1] > high[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()

    if not stack:
        ans.append(0)
    stack.append([i,high[i]])

print(' '.join(map(str,ans)))
