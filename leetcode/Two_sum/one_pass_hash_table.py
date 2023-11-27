def twoSum(nums,target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []  # No solution found

number = [2,7,11,15]
goal = 9

print(twoSum(number,goal))