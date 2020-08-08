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

    def addToStart(self, value):
        current = self.head
        node = Element(value)
        current.prev = node
        node.next = current
        self.head = node
        self.sizeOfLinkedList += 1
        return None

    def getPosition(self, position):
        current = self.head
        currPosition = 0
        if position > self.sizeOfLinkedList:
            return "Size exceeds the length of Linked List " + str(ll.sizeOfLinkedList)
        else:
            while current:
                currPosition += 1
                if currPosition == position:
                    print("Element at " + str(position) +
                          "th position is " + str(current.element))
                    return current
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.element)
            current = current.next
        return None

    def insert(self, new_element, position):
        new_element = Element(new_element)
        current = self.head
        counter = 0
        if position > self.sizeOfLinkedList:
            return "Position exceeds the length of the linked list"
        else:
            while current:
                counter += 1
                if counter == position:
                    previous = current.prev
                    new_element.next = current
                    previous.next = new_element
                    new_element.prev = previous
                    self.sizeOfLinkedList += 1
                else:
                    current = current.next
        return None

    def addToEnd(self, value):
        node = Element(value)
        current = self.head
        while current:
            if current.next != None:
                current = current.next
            else:
                current.next = node
                node.prev = current
                self.sizeOfLinkedList += 1
                return None

    def removeByValue(self, value):
        current = self.head
        while current:
            if current.element == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = current.next
            else:
                current = current.next
        return None

    def removeByPosition(self, position):
        valueOnPosition = self.getPosition(position)
        previousVal = valueOnPosition.prev
        nextVal = valueOnPosition.next
        nextVal.prev = previousVal
        previousVal.next = nextVal

    def findMinMax(self):
        current = self.head
        maxVal = current.element
        minVal = current.element
        while current:
            if current.element > maxVal:
                maxVal = current.element
            elif current.element < minVal:
                minVal = current.element
            current = current.next
        return "the max is: " + str(maxVal) + " and the min is: " + str(minVal)

    def count(self, value):
        pass


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.addToStart(5)
    ll.getPosition(4)
    print('The size of the linked list is: ' + str(ll.sizeOfLinkedList))
    print('Before Insertion')
    ll.display()
    print('\n')
    print('After Insertion')
    ll.insert(6, 3)
    ll.display()
    print('\n')
    print('After Removing')
    ll.removeByPosition(2)
    ll.display()
    print('\n')
    print('After appending to the end')
    ll.addToEnd(7)
    ll.display()
    print(ll.findMinMax())
    ll.count(2)
