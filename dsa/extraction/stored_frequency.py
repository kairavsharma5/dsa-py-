num=[4,3,1,2,21,3,2,24,2,12,2]
freq={}
#for i in range(0,len(num)):
#    if num[i] in freq:
#        freq[num[i]] +=1
#
#    else:
#        freq[num[i]]=1
#print(freq)
#
#tc=O(1)

n=len(num)
for i in range(0,n):
    freq[num[i]]=freq.get(num[i],0)+1
print(freq)
