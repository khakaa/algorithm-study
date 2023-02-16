import sys
from itertools import permutations

input = sys.stdin.readline
n,m,k = map(int, input().rstrip().split())
boxes = list(map(int, input().rstrip().split()))
rails = list(permutations(boxes, n))

ans = float('inf')

for rail in rails:
    total, cnt = 0, 0
    for i in range(k):
        temp = 0
        while temp <= m:
            temp += rail[cnt % n]
            cnt += 1
        cnt -= 1 # while문 안에서 m보다 큰 값까지를 더해줬기 때문에 한번씩 빼준다
        temp -= rail[cnt % n]
        total += temp
    ans = min(ans, total)

print(ans)
