n=4
m=26

low=0
high=m
while(low<=high):
    mid=(low+high)/2
    a=(mid**n)
    if (a==m):
        print(mid)
        break
    elif(a>m):
        high=mid
    else:
        low=mid
    