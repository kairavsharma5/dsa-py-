#check if array is sorted or not return t and f
nums=[55,123,210,1,-13,-321,0]
n=len(nums)
flag=False
for i in range(0,n-1):
    if nums[i]<nums[i+1]:
        flag=True
print(flag)
        
    
