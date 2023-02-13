import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
score_sum = [0 for _ in range(N)]
ans = []

# 병합 정렬 알고리즘 -> O(NlogN)
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    l = h = 0
    merged_arr = []
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] > high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

# 대회별 등수
for s in score:
    sorted_score = merge_sort(s) # 합병 정렬
    dic = {}
    idx = 1
    for ss in sorted_score: 
        if ss not in dic: # 딕셔너리 안에 이미 있으면 넘어감 -> 중복 등수 처리
            dic[ss] = idx # (점수, 등수)로 딕셔너리 생성
        idx += 1
    arr = []
    for i in range(len(s)):
        arr.append(dic[s[i]]) # dic[대회 별 점수] -> 등수 반환
        score_sum[i] += s[i] # 합계 미리 구해놓기
    print(*arr)

# 점수 합계 등수
sorted_score_sum = merge_sort(score_sum)
idx = 1
dic = {}
for sss in sorted_score_sum:
    if sss not in dic:
        dic[sss] = idx
    idx += 1

arr = []
for i in range(len(score_sum)):
    arr.append(dic[score_sum[i]])
print(*arr)