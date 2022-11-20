T = int(input())
ans = []
tc = []

for _ in range(T):
    tc.append(input().strip())

for word in tc:
    if word == word[::-1]:
        ans.append(1)
    else:
        ans.append(0)

for i in range(T):
    print(f'#{i+1} {ans[i]}')
