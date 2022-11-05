number = input().split('-')
result = []

for n in number:
    n_sum = 0
    plus = n.split('+')

    for p in plus:
        n_sum += int(p)
    result.append(n_sum)

ans = result[0]
for i in range(1, len(result)):
    ans -= result[i]

print(ans)
