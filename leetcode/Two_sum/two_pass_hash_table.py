def twoSum(nums,target):
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(n):
        complement = target - nums[i] # 9 - [2,7,11,15]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # No solution found

number = [2,7,11,15]
goal = 9

print(twoSum(number,goal))