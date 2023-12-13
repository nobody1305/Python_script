
def twoSum(nums,target):
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution found

number = [2,7,11,15]
goal = 9

print(twoSum(number,goal))