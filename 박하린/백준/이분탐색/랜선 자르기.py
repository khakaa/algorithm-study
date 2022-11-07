K,N = map(int, input().split())
result = 0
lan = []
for _ in range(K):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for l in lan:
        total += l // mid
        # if total > N:
        #     break
        
    if total < N:
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1
print(result)

