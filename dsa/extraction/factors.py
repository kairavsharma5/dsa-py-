n=10
num=n
#res=[]
#c=1
#while (c<=n) :
#    if (num%c==0):
#        res.append(c)
#    c=c+1
#print(res)
  

#res=[]
#for i in range(1,n//2+1):
#    if num%i==0:
#        res.append(i)
#res.append(num)
#print(res)


from math import sqrt
result=[]
for i in range(1,int(sqrt(num)+1)):
    if num % i ==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
print(result)
