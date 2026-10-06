nums=[1,3,4,5,8,9,14,15,19,20,21]
n=len(nums)
target=8
floor=-1
ceil=-1
#brute
'''for i in range(0,n):
    if (nums[i]>=target):
        floor=nums[i]
        break
for i in range(0,n):
    if (nums[i]>target):
        ceil=nums[i]
        break
print(floor,ceil)'''


#OPTIMAL
low=0
high=n-1
while (low<=high):
    mid=(high+low)//2
    if (nums[mid]==target):
        floor=ceil=nums[mid]
        break
    elif(nums[mid]>target):
        ceil=nums[mid]
        high=mid-1
    else:
        floor=nums[mid]
        low=mid+1
print(floor,ceil)
