class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None            # the extra pointer that makes it doubly linked


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. insert at head
    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # 2. add at last
    def insert_at_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # 3. insert in between
    def insert_at(self, val, position):
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node = Node(val)
        new_node.next = current.next
        new_node.prev = current
        if current.next:                     # skip this when inserting at the very end
            current.next.prev = new_node
        current.next = new_node

    # 4. delete head
    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:                        # the list may now be empty
            self.head.prev = None

    # 5. delete last
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:           # only one node
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    # 6. delete in between
    def delete_in_between(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 0:
            self.delete_head()
            return

        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return

        current.prev.next = current.next
        if current.next:                     # skip this when deleting the last node
            current.next.prev = current.prev

    # 7. traverse
    def traverse(self):
        current = self.head
        while current:
            print(current.val, end=" <-> ")
            current = current.next
        print("None")