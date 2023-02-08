import sys,heapq
# n : 보석 총 개수
# m,v : 각 보석의 무게, 가격
# k : 상덕이가 가진 가방의 개수
# c : 각 가방에 담을 수 있는 최대 무게

input = sys.stdin.readline

n,k = map(int, input().rstrip().split(' '))
jewels = []
bags = []
ans = 0

# 보석 입력값 및 정렬
for _ in range(n):
    m,v = map(int, input().rstrip().split(' '))
    jewels.append((m,v))
jewels = sorted(jewels, key=lambda x : x[0])

# 가방 입력값 및 정렬
for _ in range(k):
    bags.append(int(input().rstrip()))
bags = sorted(bags) 

heap = []
for b in bags: # 가방 갯수만큼 반복
    while jewels and jewels[0][0] <= b: # 보석 무게 오름차순 정렬했으므로 첫 번째 보석 무게부터 살핌
        heapq.heappush(heap, -heapq.heappop(jewels)[1]) # 나중에 값 더해줄 때 최대힙으로 heappop해주기 위해 앞에 -를 붙여서 heapq에 넣어준다.
    if heap:
        ans -= heapq.heappop(heap)

print(ans)

# 가방은 최소힙
# 보석은 최대힙