import sys
input = sys.stdin.readline

N = int(input().rstrip())
pos = [] # 양수
neg = [] # 음수
max_sum = 0

for _ in range(N):
    n = int(input().rstrip())
    if n > 1:
        pos.append(n)
    elif n == 1:
        max_sum += 1
    else:
        neg.append(n)

pos = sorted(pos, reverse=True) # 양수는 내림차순
neg = sorted(neg) # 음수는 오름차순

# 규칙
# 1. 양, 양 : *
# 2. 음, 양 : +
# 3. 음, 음 : *
# 4. 양, 0 : +
# 5. 음, 0 : *
# 6. 양, 1 : +
# 7. 음, 1 : +

if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        max_sum += pos[i] * pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        max_sum += pos[i] * pos[i+1]
    max_sum += pos[-1]

if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        max_sum += neg[i] * neg[i+1]
else:
    for i in range(0, len(neg)-1, 2):
        max_sum += neg[i] * neg[i+1]
    max_sum += neg[-1]

print(max_sum)