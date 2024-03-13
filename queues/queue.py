class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        dequeuedNode = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            dequeuedNode.next = None

        self.length -= 1

        return dequeuedNode

    def getFirst(self):
        return self.first

    def isEmpty(self):
        return self.length == 0

    def __str__(self):
        queueStr = "["
        temp = self.first
        while temp is not None:
            queueStr += str(temp.value) + " "
            temp = temp.next

        queueStr = (queueStr[0:-1] + "]") if queueStr != "[" else "Empty"

        return queueStr

