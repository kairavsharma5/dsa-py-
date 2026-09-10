'''def func(n):
    if n==1:
        return 1
    return n + func (n-1)
x=func(5)
print(x)'''

#factorial
def func(n):
    if(n<1):
        return 1
    return n * func(n-1)
x=func(1)
print(x)