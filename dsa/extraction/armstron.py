n=111
fum=n
num=n
c=0
count=0
while(num>0):
    count=count+1
    num=num//10

arm=0
while(fum>0):
    c=fum%10
    arm=c**count+arm
    fum=fum//10
print(arm)
if(arm==n):
    print("its armstrong no.")
else:
    print("its not")