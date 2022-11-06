def solution(nums):
    count = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            sum = 0
            for k in range(j+1,len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                detect_count = 0
                for v in range(2,sum):
                    if sum % v == 0:
                        detect_count += 1
                if detect_count == 0:
                    count += 1
    return count

