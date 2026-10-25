arr=[0,3,4,7,10,9]
cows=4
arr.sort()
def canweplace (arr,dist,cows):
    n=len(arr)
    countcows=1
    last=arr[0]
    for i in range(1,n):
        if(arr[i]-last>=dist):
            countcows+=1
            last=arr[i]
    if(countcows>=cows):
        return True
    else:
        return False
for i in range(1,(max(arr)-min(arr))):
    if(canweplace(arr,i,cows)==True):
        continue
    else:
        print(i-1)
        break
print(arr[-1]-arr[0])
