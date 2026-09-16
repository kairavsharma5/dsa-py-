#right rotate by k place 
nums=[2,34,0,64,3,1,1,3]
k=int(input("how many times rotate"))
n=len(nums)
'''a=int(input("enter the time you want to rotate"))
for i in range(0,a):
    temp=nums[n-1]
    for j in range(n-2,-1,-1):
        nums[j+1]=nums[j]
    nums[0]=temp
print(nums)'''

# k is the time you want to rotate
'''rotation=k%n
for i in range(0,rotation):
    e=nums.pop()
    nums.insert(0,e)'''


#better soln
'''k=k%n
nums[:]=nums[n-k:]+nums[:n-k]
print(nums)'''


#optimal soln
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)
print(nums)