nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3

#BRUTE
"""count=0
n=len(nums)
for i in range(0,n):
    if nums[i]==target:
        count+=1
print(count)"""


#OPTIMAL
n=len(nums)
ub,lb=n,-1
low=0
high=n-1
while(low<=high):
    mid=(low+high)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1

low=0
high=n-1
while(low<=high):
    mid=(low+high)//2
    if nums[mid]>target:
        ub=mid
        high=mid-1
    else:
        low=mid+1
if lb==-1:
    print(0)
print(ub-lb)

