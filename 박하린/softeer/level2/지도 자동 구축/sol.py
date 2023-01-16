n = int(input())
side = 2

for i in range(n):
    side += 2**i

print(side**2)