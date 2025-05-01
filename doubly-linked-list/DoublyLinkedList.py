from typing import Optional


class Node:
    def __init__(self,val):
        self.val = val
        self.next:Optional[Node] = None
        self.prev:Optional[Node] = None


class DoublyLinkedList:
    def __init__(self):
        self.head:Optional[Node] = None
        self.tail:Optional[Node] = None

    def add(self,val:int):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node



    def delete(self,val:int):
        current = self.head

        while current is not None:
            if current.val == val:
                after = current.next
                before = current.prev

                if before is not None:
                    before.next = current.next

                if after is not None:
                    after.prev = current.prev

                if self.head == current:
                    self.head = after

                if self.tail == current:
                    self.tail = before

                del current
                return True

            current = current.next

        return False # means not found


    def display(self):
        current = self.head
        while current is not None:
            print(current.val,end=" <--> ")
            current = current.next


