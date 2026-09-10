def func (s,l,r):
    if(l>=r):
       print("p")
       return True
    if(s[l]!=s[r]):
        print("L")
        return False
    return func(s,l+1,r-1)
n="jalaj"
func(n,0,len(n)-1)