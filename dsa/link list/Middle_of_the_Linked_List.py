#brute

'''class Solution(object):
    def middleNode(self, head):
        n = 0
        temp = head
        while temp is not None:
            temp = temp.next
            n += 1

        temp = head
        for i in range(n // 2):
            temp = temp.next
        return temp
'''
#optimal
'''slow=head
fast=head
while(fast!=None and fast.next !=None):
    slow=slow.next
    fast=fast.next.next
return slow'''