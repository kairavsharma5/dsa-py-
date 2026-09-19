nums=[3,0,1]
n=len(nums)
'''for i in range(0,n+1):
    if i not in nums:
        nums.append(i)
        print(i,"is the no")
'''
'''freq={}
for i in range(0,n+1):
    freq[i]=0
for j in nums:
    freq[j]+=1
for k,v in freq.items():
    if v==0:
        print(k)'''
sum=0
sum1=0
sum2=0
for i in nums:
    sum=sum+i
for i in range (0,n+1):
    sum1=sum1+i
sum2=sum1-sum
print(sum2)


