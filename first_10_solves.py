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



# solve 2
# palindrome number (9)

# string approach
def isPalindrome(x:int)-> bool:
    char = str(x)
    return char == char[::-1]
print(isPalindrome(1234))

# number approach
def isPalindrome(x:int)-> bool:
    temp=x
    rev=0
    while temp > 0:
        last=temp%10
        rev= rev*10+last
        temp//=10
    return rev == x 
print(isPalindrome(1221))



# solve 3
# water bottles (1518) 

def numWaterBottles(numBottles: int, numExchange: int) -> int:
    res = numBottles
    while numBottles >= numExchange:
        numRemainder = numBottles % numExchange
        numBottles//=numExchange
        res += numBottles
        numBottles += numRemainder
    return res
print(numWaterBottles(9,3))
