#brute

'''class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        stck=[]
        temp=head
        while(temp is not None):
            stck.append(temp.val)
            temp=temp.next
        temp=head
        while(temp is not None):
            a=0
            a=stck.pop()
            if(temp.val !=a):
                return False
            temp=temp.next
        return True
    '''

#optimal
class Solution(object):
    
    def reverse(self, head):
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        # 1. find the middle (the loop from the video)
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half
        new_head = self.reverse(slow.next)

        # 3. compare the two halves
        first = head
        second = new_head
        while second is not None:
            if first.val != second.val:
                self.reverse(new_head)      # put the list back
                return False
            first = first.next
            second = second.next

        self.reverse(new_head)              # put the list back
        return True
    
        