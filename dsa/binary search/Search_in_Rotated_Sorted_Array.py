nums=[1,4,5,6,8,9,10,11,15,20]

#brute
"""n=len(nums)
target=8
index=-1
for i in range(0,n):
    if (nums[i]==target):
        index=i
print(index)"""


#OPTIMAL
target=7
n=len(nums)
low=0
high=n-1
while(low<=high):
    mid=(low+high)//2
    if (nums[mid]==target):
        print(mid)
        break
    if (nums[mid]<nums[high]):  #[5,1,3]
        if nums[mid] < target <= nums[high]:   
            low = mid + 1
        else:
            high = mid - 1
    else:
        if (nums[low]<=target<=nums[mid]):
            high=mid-1
        else:
            low=mid+1
#return -1