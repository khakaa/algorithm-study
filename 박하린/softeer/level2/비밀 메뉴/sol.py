m,n,k = map(int, input().split(' '))
s_menu = list(map(int, input().split(' ')))
user = list(map(int, input().split(' ')))
ans = 'normal'

for i in range(n):
    if user[i] == s_menu[0]:
        if user[i:i+m] == s_menu and m <= n:
            ans = 'secret'
            break
        else:
            ans = 'normal'

print(ans)