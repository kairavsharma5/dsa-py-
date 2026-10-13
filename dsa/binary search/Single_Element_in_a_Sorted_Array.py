nums=[1,1,2,2,3,4,4,8,8]
n=len(nums)
i=0
count=0
while(i<n):
    
    if (i+1<n) and (nums[i]==nums[i+1]):
        i+=2
    else:
        print(nums[i])
        break
        
    
    

    
