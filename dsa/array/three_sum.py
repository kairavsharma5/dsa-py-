arr=[-1,0,1,2,-1,4]
n=len(arr)
'''my_set=set()
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k]==0:
                b=[arr[i],arr[j],arr[k]]
                b.sort()
                my_set.add(tuple(b))
print(my_set)                '''


#better
'''result=set()
for i in range(0,n):
    my_set=set()
    for j in range(i+1,n):
        third=-(arr[i]+arr[j])
        if third in my_set:
            temp=[arr[i],arr[j],third]
            temp.sort()
            result.add(tuple(temp))
        my_set.add(arr[j])

print( result)'''


#optimal
ans=[]
n=len(arr)
arr.sort()
for i in range(0,n):
    if i!=0 and arr[i]==arr[i-1]:
        continue
    j=i+1
    k=n-1
    while j<k:
        total_sum=arr[i]+arr[j]+arr[k]
        if total_sum<0:
            j+=1
        elif total_sum>0:
            k-=1
        else:
            temp=[arr[i],arr[j],arr[k]]
            ans.append(temp)
            j+=1
            k-=1
            while j<k and arr[j]==arr[j-1]:
                j+=1
            while j<k and arr[k]==arr[k+1]:
                k-=1
print(ans)
 