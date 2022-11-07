# 조합 풀이
from itertools import combinations

N,M = map(int, input().split(' '))
city = []
home = []
chick = []

for _ in range(N):
    city.append(list(map(int, input().split(' '))))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chick.append((i,j))

print(home, chick)
min_len = float('inf')
for comb in combinations(chick, M):
    ch_len = 0
    for h in home:
        ch_len += min([abs(ch[0]-h[0]) + abs(ch[1]-h[1]) for ch in comb])
        if ch_len >= min_len:
           break
    if ch_len < min_len:
        min_len = ch_len
            
print(min_len)