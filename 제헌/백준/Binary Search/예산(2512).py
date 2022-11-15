n = int(input())
data = list(map(int, input().split()))
m = int(input())
res = []
start, end = 0, max(data)

while start <= end:
    mid = (start + end) // 2
    money = 0

    for a in data:
        if a >= mid:
            money += mid
        
        else:
            money += a
    
    if money <= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)