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