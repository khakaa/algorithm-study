def binary_search(start, end):
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        house_now = house_arr[0]
    
        for i in range(1, len(house_arr)):
            if house_arr[i] >= house_now + mid:
                print(mid)
                house_now = house_arr[i]
                cnt += 1
        if cnt >= c:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

n, c = map(int, input().split())

house_arr = [int(input()) for _ in range(n)]
house_arr.sort()

start, end = 1, house_arr[-1] - house_arr[0]

print(binary_search(start, end))