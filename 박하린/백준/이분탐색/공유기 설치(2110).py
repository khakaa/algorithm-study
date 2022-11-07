import sys

n,c = map(int, input().split(' '))
router = []
result = 0

for _ in range(n):
    router.append(int(sys.stdin.readline()))

router.sort()

start = 1 # 최소 거리
end = router[-1] - router[0] # 최대 거리

while start <= end:
    mid = (start + end) // 2 # 최대 거리 이진탐색으로 구하기
    current = router[0] # 집의 좌표 최소
    count = 1

    for i in range(1, n):
        if router[i] - current >= mid: # 거리 차가 mid 이상인 것 개수 구하기
            count += 1
            current = router[i]
    
    # 개수가 c보다 많을 때 시작값 크게
    if count >= c:
        start = mid + 1
        result = mid

    # 개수가 c보다 적을 때 종료값 작게
    else:
        end = mid - 1

print(result)
