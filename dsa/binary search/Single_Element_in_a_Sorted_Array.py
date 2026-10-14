nums=[1,1,2,2,3,4,4,8,8]
n=len(nums)
"""#BRUTE

i=0
count=0
while(i<n):
    
    if (i+1<n) and (nums[i]==nums[i+1]):
        i+=2
    else:
        print(nums[i])
        break"""
        

#OPTIMAL

low=1
high=n-2
if (n==1):
    print(nums[0])
elif(nums[0]!=nums[1]):
    print(nums[0])
elif(nums[n-1]!=nums[n-2]):
    print(nums[n-1])
while(low<=high):
    mid=(low+high)//2
    if (nums[mid]==nums[mid-1]) or (nums[mid] ==nums[mid+1]):
        if(((mid)%2==1) and (nums[mid]==nums[mid-1]) or(mid%2==0) and (nums[mid]==nums[mid+1])):
            low=mid+1
        else:
            high=mid-1
    else:
        print(nums[mid])
        break
