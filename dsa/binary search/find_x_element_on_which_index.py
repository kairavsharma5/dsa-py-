nums=[2,4,6,7,9,11,18,19]
n=len(nums)
#iterative soln
'''def binary_search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if (nums[mid]==target):
            return mid
        elif(nums[mid]<=target):
            low=mid+1
        else:
            high=mid-1
    return -1'''


#RECURSIVE SOLN
def binary_search(nums,low,high):
    if low>high:
        return-1
    mid=(low+high)//2
    if (nums[mid]==target):
        return(mid)
    elif(nums[mid]< target):
        return binary_search(nums,mid+1,high)
    else:
        return binary_search(nums,low,mid-1)
    

target=2
a=binary_search(nums,0,n-1)
print(a)