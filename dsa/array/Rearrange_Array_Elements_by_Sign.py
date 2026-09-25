nums=[3,2,-1,-4,5,-6]
'''pos=[]
neg=[]
result=[]
n=len(nums)
for i in range(0,n):
    if nums[i]>=0:
        pos.append(nums[i])
    else:
        neg.append(nums[i])
k=0
while(k<(n/2)):
    result.append(pos[k])
    result.append(neg[k])
    k+=1
print(result)'''

n=len(nums)
result=[0]*n
pos,neg=0,1
for i in range(0,n):
    if nums[i]>=0:
        result[pos]=nums[i]
        pos+=2
    else:
        result[neg]=nums[i]
        neg+=2
print(result)
