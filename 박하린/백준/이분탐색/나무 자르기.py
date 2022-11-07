n, m = map(int, input().split())
tree = list(map(int, input().split()))
result = 0

start = 0
end = max(tree)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for t in tree:
        if t > mid:
            total += t - mid
        if total > m: # 시간초과땜에 추가
            break

    # 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    
    # 남는 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid
        start = mid + 1
    # print(start,mid,end,total)

print(result)