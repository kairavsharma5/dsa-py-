n=234213
num=n
c=0
while (num>0):
    c=(c*10)+num%10
    num=num//10

print(c)
if (c==n):
    print("its palindrome")
else:
    print("its not a palindrome")
