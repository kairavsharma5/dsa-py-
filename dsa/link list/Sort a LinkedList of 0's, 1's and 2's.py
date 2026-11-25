def sortList012(head):
    if head is None or head.next is None:
        return head

    zero_head = ListNode(-1)       # dummy heads, one per value
    one_head = ListNode(-1)
    two_head = ListNode(-1)

    zero = zero_head               # tail pointers
    one = one_head
    two = two_head

    temp = head
    while temp is not None:
        if temp.val == 0:
            zero.next = temp
            zero = temp
        elif temp.val == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next

    # join: zeros -> ones -> twos
    zero.next = one_head.next if one_head.next else two_head.next
    one.next = two_head.next
    two.next = None                # cut any old link, or you get a cycle

    return zero_head.next
