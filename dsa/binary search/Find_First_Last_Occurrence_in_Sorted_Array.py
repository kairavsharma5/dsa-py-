nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
'''
first,last=-1,-1
target=3
n=len(nums)
for i in range(0,n):
    if (nums[i]==target):
        if (first==-1):
            first=i                             #TC=O(n) but wants log n
        last=i
print(first,last)'''



#OPTIMAL
def lowerBound( nums, target):
        n = len(nums)
        lb = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

def upperBound(nums, target):
    n = len(nums)
    ub = n
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    return ub
def searchRange( nums, target):
        lb = lowerBound(nums, target)
        if lb==-1:
             return -1,-1
        ub = upperBound(nums, target)
        return lb, ub-1

target=11
a=searchRange(nums,target)
print(a)