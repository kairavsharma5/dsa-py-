from math import ceil
piles=[3,6,7,11]
h=8
b=max(piles)
n=len(piles)
def func(piles,hourly):
    total_hrs=0
    for i in range(0,n):
        total_hrs+=ceil(piles[i]/hourly)
    return total_hrs

#BRUTE
"""for i in range(1,b+1):
    req_time=func(piles,i)
    if(req_time<=h):
        print(i)
        break"""



#OPTIMAL
low=1
high=max(piles)
while(low<=high):
    mid=(low+high)//2
    totalhrs=func(piles,mid)
    if(totalhrs<=h):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
