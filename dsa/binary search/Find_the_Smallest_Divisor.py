from math import ceil
threshold=6
arr=[1,2,5,9]
def func(arr,div):
    a=0
    for i in range(0,len(arr)):
        a+= ceil(arr[i]/div)
    return a
n=len(arr)
if(n==0):
    print(-1)
if(n==1):
    print[0]
low=1
high=max(arr)
ans=low
while(low<=high):
    mid=(low+high)//2
    if (func(arr,mid)<=threshold):
        ans =mid
        high=mid-1
    else:
        low=mid+1
print(ans)