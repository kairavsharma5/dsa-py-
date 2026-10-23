bloomDay=[7,7,7,7,13,11,12,7]
m,k=2,3
#BRUTE



def func(bloomDay, day, m, k):
    counte = 0
    no_of_bouquet = 0
    for i in range(0, len(bloomDay)):
        if(bloomDay[i] <= day):
            counte += 1
        else:
            no_of_bouquet += counte // k   # first copy: runs when a closed flower ends a group
            counte = 0
        no_of_bouquet += counte // k           # second copy: runs once, after the loop
        return no_of_bouquet
n=len(bloomDay)
if ((m*k)>n):
    print(-1)
    
            
"""for i in range(min(bloomDay),max(bloomDay)+1):
           if (func(bloomDay,i,m,k)>=m):
                return(i) """   

low=min(bloomDay)
high=max(bloomDay)
ans=high
while(low<=high):
    mid=(low+high)//2
    if(func(bloomDay,mid,m,k)>=m):
        ans=mid
        high=mid-1
    else:
                
        low=mid+1
print(ans)