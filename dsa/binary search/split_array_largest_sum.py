arr=[12,34,67,90]
students=2
def func(mid,students):
    allocated_stu=1
    pages=0
    for i in range(0,len(arr)):
        if(arr[i]>mid):
            return False
        if(pages+arr[i]>mid):
            allocated_stu+=1
            pages=arr[i]
        else:
            pages+=arr[i]
    if(allocated_stu>students):
        return False
    else:
        return True
low=min(arr)
high=sum(arr)
while(low<=high):
    mid=(low+high)//2
    if(func(mid,students)==True):
        high=mid-1
        ans=mid
    else:
        low=mid+1
print(ans)


#painters problem is same