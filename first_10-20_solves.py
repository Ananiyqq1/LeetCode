# solve 11
# binary tree inorder traversal (94)

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    # Iterative Solution
    stack = []
    ans = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right
    return ans

def insertLevelOrder(arr: List[int], root: Optional[TreeNode], i: int, n: int) -> Optional[TreeNode]:
    # Helper function to insert nodes in level order
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

# Create a binary tree from a list
arr = [1, 4, 2, 3]
n = len(arr)
root = insertLevelOrder(arr, None, 0, n)

# Perform inorder traversal
print(inorderTraversal(root))  # Output: [3, 4, 1, 2]



# solve 12 
#  product of array except itself (238)
def productExceptSelf(nums: list[int]) -> list[int]:
    r =[1]
    for i in range(len(nums)-1,0,-1):
        r.append(nums[i]*r[-1])
    r = r[::-1]
    l = 1
    for i in range(len(nums)):
        r[i] = r[i]*l
        l *= nums[i]
    return r
print(productExceptSelf([1,2,3,4]))



# solve 13
# crawler log folder (1598)
def minOperations(logs: List[str]) -> int:
    d = 0
    for i in logs:
        if i == "./": continue
        elif i =="../":
            d-=1
            if d < 0: d = 0
        else:
            d+=1
    return d
print(minOperations(["d1/","d2/","../","d21/","./"]))



# solve 14
# reverse integer (7)
def reverse(x: int) -> int:
    rev=0
    is_Negative = x < 0
    if is_Negative:
        x = abs(x)
    while x > 0:
        rem = x % 10 
        rev = rev*10 + rem
        x//=10
    if rev < -2**31 or rev > 2**31-1:
        return 0
    if is_Negative:
        return -rev
    return rev
print(reverse(1243))



# solve 15
# remove element (27)
def removeElement(nums: List[int], val: int) -> int:
    index = 0
    for i in range(0,len(nums)):
        if nums[i]!= val:
            nums[index] = nums[i]
            index+=1
    return index
print(removeElement([3,2,2,3],3))



# solve 16
# permutations (46)
def permute(nums: List[int]) -> List[List[int]]:
    def track(s):
        if s == len(nums):
            ans.append(nums.copy())
            return
        for i in range(s,len(nums)):
            nums[s],nums[i] = nums[i],nums[s]
            track(s+1)
            nums[s],nums[i] = nums[i],nums[s]
    ans = []
    track(0)
    return ans  
print(permute([1,2,3]))



# solve 17
# perfect number (507)
def checkPerfectNumber(num: int) -> bool:
    ans = 0
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            ans+=i
            if i*i!=num:
                ans+=num//i
    return bool(ans - num)
print(checkPerfectNumber(28))



# solve 18
# sum of left leaves (404) 
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def dfs(node, is_left):
        nonlocal total
        if not node:
            return

        if not node.left and not node.right:
            if is_left:
                total += node.val
            return

        dfs(node.left, True)
        dfs(node.right, False)

    total = 0
    dfs(root, False)
    return total

def buildTree(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    stack = [root]
    i = 1

    while stack and i < len(values):
        node = stack.pop(0)

        if i < len(values) and values[i] != None:
            node.left = TreeNode(values[i])
            stack.append(node.left)
        i += 1

        if i < len(values) and values[i] != None:
            node.right = TreeNode(values[i])
            stack.append(node.right)
        i += 1

    return root

root = buildTree([3, 9, 20, None, None, 15, 7])

print(sumOfLeftLeaves(root))  



# solve 19
# pow(x,n) (50)
def myPow(x: float, n: int) -> float:
# LINEAR APPROACH
    if n == 0: return 1
    p = 1
    is_negative = n < 0 
    n = abs(n)
    for i in range(n):
        if n > 0:
            p*=x
        elif is_negative:
            p=(1/p*x)
    if is_negative: return 1/p
    else: return p
print(myPow(2,7))        
# RECURSIVE APPROACH
def fun(x,n):
    if x==0: return 0
    if n==0: return 1
    elif n%2: 
        ans = fun(x,(n-1)//2)
        return ans * ans *x
    else:
        ans = fun(x,n//2)
        return ans*ans
    p = fun(x,abs(n))
    if n >= 0: return p 
    else: return 1/p 
print(fun(4,6))



# solve 20
# grey code (89)
def grayCode(n: int) -> List[int]:
    ans = []
    for x in range(2**n):
        ans.append(x^(x>>1))
    return ans
print(grayCode(3))















