class Solution(object):
    def findMiddle(self, head):
        slow = head
        fast = head.next                    # fast starts one step ahead
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow                         # end of the first half

    def merge(self, list1, list2):
        dummy = ListNode(-1)
        temp = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        if list1:
            temp.next = list1               # attach whatever is left
        else:
            temp.next = list2
        return dummy.next

    def sortList(self, head):
        if head is None or head.next is None:    # the highlighted line
            return head

        middle = self.findMiddle(head)
        right = middle.next
        middle.next = None                  # cut the list in two
        left = head

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)