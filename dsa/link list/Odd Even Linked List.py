#OPTIMAL
"""if(head is none or head.next is none):
    return head
odd=head
even=head.next
even_head=even
while(even is not None and even.next is not None):
    odd.next=odd.next.next
    odd=odd.next
    even.next=even.next.next
    even=even.next
odd.next=even_head
return head"""