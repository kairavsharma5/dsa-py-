nums=[1,1,1,0,0,1,1,1,1,0,1,1]
temp,count=0,0
n=len(nums)
for i in range(0,n):
    if nums[i]==1:
        temp+=1

    else:
        temp=0
    if temp>count:
        count=temp
print(count)
