T = int(input())
ans = []
tc = []
for _ in range(T):
    tc.append(list(map(int, (input().split(' ')))))

# p : A사 1L당 요금
# q : B사 rL이하 기본요금
# s : B사 rL이상 1L당 요금
# w : 사용량

for p,q,r,s,w in tc:
    a_fee = p * w
    b_fee = q
    if w-r > 0:
        b_fee += (w-r)*s
    ans.append(min(a_fee,b_fee))

for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')