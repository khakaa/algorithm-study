def solution(nums):
    answer = set(nums)
    if len(nums)//2 > len(answer):
        return len(answer)
    else:
        return len(nums)//2
print(solution)