N = int(input())
count = 0
total = 0

for i in range(1, N+1):
    total += i
    count += 1

    # 200의 경우 count=18, total=171인데, 200 - 171값을 더해주면 200이 되므로 답은 19가되는 원리
    if total > N:
        count -= 1
        break

print(count)
