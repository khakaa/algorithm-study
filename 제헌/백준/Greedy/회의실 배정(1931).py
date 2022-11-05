N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end_pivot = 0

for i, j in time:
    if i >= end_pivot:
        cnt += 1
        end_pivot = j

print(cnt)