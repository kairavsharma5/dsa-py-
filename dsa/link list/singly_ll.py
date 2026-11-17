class node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=node(5)
node2= node(11)
node3=node(21)

node1.next=node2
node2.next=node3
print(node1.val)
print(node1.next)
print(node1.next.val)