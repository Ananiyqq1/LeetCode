# solve 1
# TWO SUM (1)

# brute force approach
def twoSum(nums: list[int],target: int)-> list[int]:
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]  
print(twoSum([1,2,3,4,5], 6))

# hash map approach
def twoSum(nums: list[int],target:int)-> list[int]:
    map = {}
    for i in range(len(nums)):
        if nums[i] not in map:
            map[target-nums[i]] = i
        else:
            return [map[nums[i]],i]
print(twoSum([1,2,3,4,5],6))


