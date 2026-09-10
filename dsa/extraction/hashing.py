n=[1,2,3,4,5,7,8,4,2,4,2,2,1,1]
m=[10,111,1,9,89,12]
freq={}
#for num in m:
#    count=0
#    for x in n:
#        if num ==x :
#            count+=1
#    print(count)



#hash_list=[0,0,0,0,0,0,0,0,0,0,0]
#for num in n:
#    hash_list[num]+=1
#for num in m :
#    if num<1 or num>10:
#        print(0)
#    else:
#        print(hash_list[num])


for i in range(0,len(n)):
    freq[n[i]]=freq.get(n[i],0)+1
result={}
for x in range(0,len(m)):
    val=m[x]
    if val<0 or val>10:
          result[val]=0
    else:
         result[val]=freq.get(val,0)
print(result)