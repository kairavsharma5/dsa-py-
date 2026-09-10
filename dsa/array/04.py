#count of unique elements
nums=[1,1,1,2,2,3,3,3,4,5,6,9]
n=len(nums)
"""freq_map={}
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
print(freq_map)
for k in freq_map:
    nums[j]=k
    j+=1
print(j,"unique elements")"""


#the another soln will be that by two pointers consider i at start and then j after it increase j
#when a unique no. founded than i then increase i by one and swap then keep on inc j
#when j exits the array exit everything stop i will be the count
if n==1:
    print(1)
i=0
j=i+1
while j<n:
    if nums[j]!=nums[i]:
        i+=1
        nums[i],nums[j]=nums[j],nums[i]
    j+=1
i+=1
print(nums)
print(i)