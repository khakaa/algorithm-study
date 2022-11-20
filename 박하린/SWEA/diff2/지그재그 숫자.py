T = int(input())
ans = []
tc = []

for _ in range(T):
    tc.append(int(input()))

for n in tc:
    i = 2
    zigzag = 1
    
    if n == 1:
        ans.append(1)
        continue

    while i <= n:
        if i % 2 == 1:
            zigzag += i
        else:
            zigzag -= i
        i += 1
    ans.append(zigzag)

for i in range(T):
    print(f'#{i+1} {ans[i]}')

