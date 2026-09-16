#right rotate an array by one place
nums=[55,123,210,1,-13,-321,0]
n=len(nums)
#nums[:]=[nums[-1]]+nums[0:n-1]
temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp

print(nums)
