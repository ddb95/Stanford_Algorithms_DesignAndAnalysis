class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Gets the current value
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def isEmpty(self):
        if self.head == None or self.head.value == None:
            return True
        else:
            return False

    def addToStart(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def get_position(self, position):
        counter = 0
        current = self.head
        while current:
            counter = counter + 1
            if counter == position:
                if current.value != None:
                    return current
            else:
                current = current.next

    def insert(self, new_element, position):
        counter = 0
        current = self.head
        while current:
            counter = counter + 1
            if counter == position-1:
                previousValue = current
                nextValue = current.next
                new_element.next = nextValue
                previousValue.next = new_element
            else:
                current = current.next

    def removeByValue(self, value):
        current = self.head
        while current.next:
            if current.value == value:
                current.value = current.next.value
                current.next = current.next.next
            else:
                current = current.next

    def removeByPosition(self, position):
        current = self.head
        counter = 0
        while current:
            counter = counter + 1
            if counter == position:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return

    def displayAllValues(self):
        current = self.head
        while current:
            if current.value:
                print(current.value)
                current = current.next
        return

    def lengthOfList(self):
        current = self.head
        counter = 0
        while current.value != None:
            if current.value:
                counter = counter + 1
                if current.next == None:
                    return counter
                else:
                    current = current.next

    def findMaxMin(self):
        current = self.head
        lowestValue = current.value
        greatestValue = current.value
        while current:
            if current.value < lowestValue:
                lowestValue = current.value
            elif current.value > greatestValue:
                greatestValue = current.value
            current = current.next
        return 'lowestValue: ' + str(lowestValue) + ' greatestValue: ' + str(greatestValue)

    def addToEnd(self, value):
        current = self.head
        while current:
            if current.next != None:
                current = current.next
            else:
                current.next = value
                return 'Added to the end'

    def count(self, value):
        current = self.head
        counter = 0
        while current:
            if current.value == value:
                counter = counter + 1
                current = current.next
            else:
                current = current.next
        return "The Element " + str(value) + " occurs " + str(counter) + " times"

    def pop(self):
        current = self.head
        while current:
            if current.next == None:
                previous.next = None
                return 'Last Element Popped'
            else:
                previous = current
                current = current.next

    def toString(self):
        current = self.head
        displayString = ''
        while current:
            displayString += str(current.value) + ' '
            current = current.next
        return displayString

    def index(self, value):
        current = self.head
        counterValue = 0
        while current:
            counterValue += 1
            if current.value == value:
                print('The index of the value: ' + str(value) +
                      ' is : ' + str(counterValue))
                current = current.next
            else:
                current = current.next
        return None

    def copy(self, linkedList):
        self = linkedList
        return linkedList

    def clear(self):
        self.head = None
        return self

    def toList(self):
        listValue = []
        current = self.head
        while current:
            listValue.append(current.value)
            current = current.next
        return listValue

    def toSet(self):
        setValue = set()
        current = self.head
        while current:
            setValue.add(current.value)
            current = current.next
        return setValue

    def sort(self):
        current = self.head
        elements = self.toList()
        elements.sort()
        counter = 0
        while current and (counter < len(elements)):
            current.value = elements[counter]
            counter += 1
            current = current.next
        return self

    def reverse(self):
        current = self.head
        elements = self.toList()
        elements.sort(reverse=True)
        counter = 0
        while current and (counter < len(elements)):
            current.value = elements[counter]
            counter += 1
            current = current.next
        return self


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)
    e6 = Element(6)
    e7 = Element(7)
    e8 = Element(8)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll2 = LinkedList()
    ll.append(e2)
    ll.append(e3)
    # Test insert
    ll.insert(e4, 3)
    ll.insert(e5, 2)
    ll.insert(e6, 6)
    # Should print 4 now
    # print(ll.get_position(1).value)
    # print(ll.get_position(2).value)
    # print(ll.get_position(3).value)
    # print(ll.get_position(4).value)
    # print(ll.get_position(5).value)
    # print(ll.get_position(6).value)

    # Test removeByValue
    # ll.removeByValue(3)
    # print('removeByValued')

    # print(ll.get_posit
    # print(ll.isEmpty())

    ll.addToStart(e7)
    ll.addToEnd(e8)
    # print(ll.get_position(1).value)
    # print(ll.get_position(2).value)
    # print(ll.get_position(3).value)
    # print(ll.get_position(4).value)
    # print(ll.get_position(5).value)
    # print(ll.get_position(6).value)
    # print(ll.get_position(7).value)
    # ll.removeByPosition(4)

    # print('Before Pop')
    # ll.displayAllValues()
    # print(ll.findMaxMin())
    # print(ll.count(3))
    # ll.pop()
    # print('After Pop')
    # ll.displayAllValues()
    # print(ll.toString())
    # ll.index(4)
    # ll2 = ll2.copy(ll)
    # ll.clear()
    # ll.displayAllValues()
    # print(ll.toList())
    # print(ll.toSet())
    # ll.sort()
    # ll.reverse()
    ll.displayAllValues()
