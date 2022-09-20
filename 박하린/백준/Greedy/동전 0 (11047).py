N, K = map(int, input().split())

coin = []
result = 0

for _ in range(N):
    coin.append(int(input()))

for c in coin[::-1]:
    if K // c == 0:
        continue

    result += K // c
    K %= c

    if K == 0:
        break

print(result)