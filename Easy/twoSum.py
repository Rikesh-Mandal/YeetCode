def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return [seen[compliment], i]
        seen[num] = i

    return False


nums = [2,5,1,66,3]
target = 69
print(twoSum(nums,target))