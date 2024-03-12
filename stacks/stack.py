class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# stack implemented with linked list
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value) -> None:
        newNode = Node(value)

        newNode.next = self.top
        self.top = newNode
        self.height += 1

    def pop(self) -> int:
        if self.isEmpty():
            return None

        oldTop = self.top
        self.top = self.top.next
        oldTop.next = None

        self.height -= 1
        return oldTop

    def isEmpty(self) -> bool:
        return self.height == 0

    def __str__(self):
        temp = self.top
        stackStr = ""
        while temp is not None:
            stackStr += str(temp.value) + "\n"
            temp = temp.next

        return "Empty" if stackStr == "" else stackStr


# stack implemented with array
class StackArray:
    def __init__(self):
        self.stack = []
        self.height = 0

    def push(self, value):
        self.stack.append(value)
        self.height += 1

    def pop(self):
        if self.isEmpty():
            return None

        self.height -= 1
        return self.stack.pop()

    def isEmpty(self):
        return self.height == 0

    def __str__(self):
        stackStr = ""
        for i in range(self.height - 1, -1, -1):
            stackStr += str(self.stack[i]) + "\n"

        return "Empty" if stackStr == "" else stackStr

