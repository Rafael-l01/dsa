class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            newNode.prev = self.tail
            self.tail = newNode

        self.length += 1
        return True

    def pop(self):
        if self.head == None:
            return None

        temp = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev

            temp.prev = None
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
            self.head.prev = newNode
            self.head = newNode

        self.length += 1
        return True

    def popFirst(self):
        if self.head == None:
            return None

        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        if index < (self.length / 2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

        # if index < 0:
        #     return None

        # i = 0
        # current = self.head
        # while current is not None:
        #     if i == index:
        #         return current
        #     current = current.next
        #     i += 1

        # return None

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
        before = self.get(index - 1)
        after = before.next

        before.next = newNode
        newNode.prev = before

        newNode.next = after
        after.prev = newNode

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.popFirst()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before

        temp.prev = None
        temp.next = None

        self.length -= 1
        return temp

    def getValues(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def getValuesReversed(self):
        values = []
        current = self.tail
        while current is not None:
            values.append(current.value)
            current = current.prev
        return values

    def __str__(self):
        listStr = "["
        current = self.head
        while current is not None:
            listStr += str(current.value) + ", "
            current = current.next

        listStr = listStr[0:-2] + "]" if listStr != "[" else "[]"

        return listStr

