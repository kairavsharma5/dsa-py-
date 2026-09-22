nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
sum1=float("-inf")
for i in range(0,n):
     temp=0
     for j in range(i,n):
          temp=nums[j]+temp
          sum1=max(sum1,temp)
print(sum1)