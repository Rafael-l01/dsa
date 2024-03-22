class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
        return True

    def pop(self):
        if self.head == None:
            return None

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None

            self.length -= 1
            return temp

        pre = self.head
        temp = self.head
        while temp.next != None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length -= 1
        return temp

    def prepend(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self.length += 1
        return True

    def popFirst(self):
        if self.head == None:
            return None

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None

            self.length -= 1
            return temp

        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current
            current = current.next
            i += 1

        return None

    def setValue(self, index, value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        newNode = Node(value)
        temp = self.get(index - 1)
        newNode.next = temp.next
        temp.next = newNode

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.popFirst()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index - 1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        before = None

        while temp is not None:
            after = temp.next

            temp.next = before
            before = temp
            temp = after

        self.tail = self.head
        self.head = before

    def getValues(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def __str__(self):
        listStr = "[ "

        current = self.head
        while current is not None:
            listStr += str(current.value) + " -> "
            current = current.next

        listStr = "[]" if listStr == "[ " else listStr[0:-3] + "]"
        return listStr

