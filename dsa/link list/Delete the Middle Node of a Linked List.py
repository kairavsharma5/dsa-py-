# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        temp=head
        count=0
        while(temp is not None):
            count+=1
            temp=temp.next
        temp=head
        val=1
        while(val<(count//2)):
            temp=temp.next
            val+=1
        temp.next=temp.next.next
        return head



#optimal
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next.next          # start fast one step ahead
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next     # slow is the node before the middle
        return head
