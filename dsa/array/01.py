#lagrest element in array
nums=[55,123,210,1,-13,-321,0]
largest=nums[0]
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
print(largest)