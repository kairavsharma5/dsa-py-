nums=[1,2,1,3,5,6,4]

#brute
'''n=len(nums)
for i in range(0,n):
    if((i==0) or (nums[i-1]<nums[i])) and((i==n-1) or (nums[i]>nums[i+1])):
        print(i)'''



#OPTIMAL
n=len(nums)
low=1
high=n-2
if(n==1):
    print(0)
if(nums[0]>nums[1]):
    print(0)
if(nums[n-1] >nums[n-2]):
    print(n-1)
while(low<=high):
    mid=(low+high)//2
    if(nums[mid]>nums[mid-1])& (nums[mid]>nums[mid+1]):
        print(mid)
        break
    elif(nums[mid]>nums[mid-1]):
        low=mid+1
    else:
        high=mid-1
