class Element(object):
    __slots__ = 'element', 'prev', 'next'

    def __init__(self, element=None, prevNode=None, nextNode=None):
        self.element = element
        self.prev = prevNode
        self.next = nextNode


class DoublyLinkedList(object):
    sizeOfLinkedList = 0

    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        current = self.head
        node = Element(value)
        if current:
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            self.sizeOfLinkedList += 1
        else:
            self.head = node
            self.sizeOfLinkedList += 1


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print('The size of the linked list is: ' + str(ll.sizeOfLinkedList))
