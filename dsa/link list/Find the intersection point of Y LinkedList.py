#brute

'''def getIntersectionNode(headA, headB):
    seen = set()
    temp = headA
    while temp is not None:
        seen.add(temp)
        temp = temp.next

    temp = headB
    while temp is not None:
        if temp in seen:
            return temp
        temp = temp.next
    return None'''

#better
def collison (t1,t2,d):
    while(d):
        d-=1
        t2=t2.next
    while(t1!=t2):
        t1=t1.next
        t2=t2.next
    return t1
t1=head1
t2=head2
n1,n2=0,0
while(t1 is not None):
    n1+=1
    t1=t1.next
while(t2 is not None):
    n2+=1
    t2=t2.next
if(n1<n2):
    return collison(head1,head2,n2-n1)
else:
    return collison(head2,head1,n1-n2)
