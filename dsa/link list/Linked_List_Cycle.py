#BRUTE
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        my_set=set()
        temp=head
        while (temp is not None):
            if (temp.next not in my_set):
                my_set.add(temp.next)
                temp=temp.next
            else:
                return True
        return False

#OPTIMAL
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while(fast is not None and fast.next is not None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
