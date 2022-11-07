# 폰켓몬

def solution(nums):
    array = set(nums)
    result = 0
    if len(nums)//2 > len(array):
        result = len(array)
    else:
        result = len(nums)//2
    return result