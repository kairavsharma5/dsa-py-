''' def goat(x,n):
    if n==0:
        return
    print(x)

    goat(x,n-1)
goat(20,4) '''

#print 1 to n 
''' func(i,n):
    if (i>n):
        return
    print(i)
    func(i+1,n)
func(1,5)'''


  # print n to 1
'''def func(n):
    if n==0:
        return
    print(n)
    func(n-1)
func(8)
    '''

# sum of 1 to n
def func(sum,i,n):
    if i>n:
        print(sum)
        return
    func(sum+i,i+1,n)
func(0,2,5)