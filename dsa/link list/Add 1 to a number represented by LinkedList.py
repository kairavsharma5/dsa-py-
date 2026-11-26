'''def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def addOne(head):
    head = reverse(head)            # last digit is now first

    temp = head
    prev = None
    carry = 1                       # the "+ 1"
    while temp is not None:
        total = temp.val + carry
        temp.val = total % 10       # digit to keep
        carry = total // 10         # carry to the next digit
        prev = temp
        temp = temp.next
        if carry == 0:              # nothing left to carry, stop early
            break

    if carry:                       # carry left over after the last digit
        prev.next = ListNode(carry) # e.g. 999 -> 1000 needs a new node

    return reverse(head)            # restore the original order'''


#OPTIMAL
def helper(temp):
    if (temp==None):
        return 1
    carry=helper(temp.next)
    temp.val+=carry
    if(temp.val<10):
        return 0
    temp.val=0
    return 1

carry=helper(head)
if (carry==1):
    newnode=Newnode(1)
    newnode.next=head
    return newnode
return head