#find second largest in an array
nums=[55,123,210,1,-13,-321,0]
largest=float("-inf")
s_largest=float("-inf")
'''for i in range(0,n):
    largest=max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]<largest:
        s_largest=nums[i]
print(largest,s_largest)'''
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        s_largest=largest
        largest=nums[i]
    elif nums[i]>s_largest and nums[i]!=largest:
        s_largest=nums[i]
print(largest,s_largest)