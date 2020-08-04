class Element(object):
    __slots__ = 'element', 'prev', 'next'

    def __init__(self, element=None, prevNode=None, nextNode=None):
        self.element = element
        self.prev = prevNode
        self.next = nextNode


class DoublyLinkedList(object):
    def __init__(self, header=None, trailer=None):
        self.header = header
        self.trailer = trailer

    def append(self, value):
        current = self.header
        if self.header and self.trailer:
            return 'sa'
        else:
            self.header.next = value
            self.trailer.prev = value


if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    ll = DoublyLinkedList()
    ll.append(e1)
    ll.append(e2)
