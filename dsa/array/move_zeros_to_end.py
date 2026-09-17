nums=[1,0,2,4,3,0,0,3,5,1]
'''n=len(nums)
temp=[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz=len(temp)
for i in range(0,nz):
    nums[i]=temp[i]
for i in range(nz,n):
    nums[i]=0'''


#optimal

i = 0
while i < len(nums) and nums[i] != 0:   # advance i to the FIRST zero
    i += 1

j = i + 1
while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1

print(nums)
