nums=[3,3]
target=6
n=len(nums)
dict={}
'''for i in range(0,n):
    for j in range(i+1,n):
        if (nums[i]+nums[j]==target):
            print(i,j)'''
#tc=o(n^2)


#optimal
for i in range(0,n):
    rem=target-nums[i]
    if rem in dict:
        print(dict[rem],i)
    dict[nums[i]]=i
