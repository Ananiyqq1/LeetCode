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



# solve 4
# plus one (66)

def plusOne(digits: list[int]) -> list[int]:
    numvar = int("".join([str(d)for d in digits]))+1
    return [int(d) for d in str(numvar)]
print(plusOne([1,2,3]))



# solve 5
# valid parentheses (20)
def isValid(s: str) -> bool:
    stack = []
    paren = {"}":"{","]":"[",")":"("}
    for c in s:
        if c in paren.values():
            stack.append(c)
        elif stack and paren[c] == stack[-1]:
            stack.pop()
        else:
            return False
    return stack == []            
print(isValid("{][]}"))



# solve 6
def mySqrt(x: int) -> int:
#ONLY WORKS FOR PERFECT SQUARES 
    t = 1
    while t * t < x:
        t = (t + x/t)/2
    return int(t)
print(mySqrt(16))
def mySqrt(x: int) -> int:
# GENERAL APPROACH
    epsilon = 0.01
    low = 0.0
    high = max(x,1)
    ans = (high + low)/2.0
    if x == 1 :return 1
    while abs(ans*ans - x) >= epsilon and ans <= x:
        if ans*ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0         
    return int(ans)
print(mySqrt(157))
