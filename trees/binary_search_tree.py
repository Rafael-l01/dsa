class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root == None:
            self.root = newNode
            return True

        temp = self.root
        while True:
            if newNode.value == temp.value:
                return False

            if newNode.value < temp.value:
                if temp.left == None:
                    temp.left = newNode
                    return True

                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = newNode
                    return True

                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True

            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def rContains(self, value):
        return self.__rContains(self.root, value)

    def __rContains(self, currentNode, value):
        if currentNode == None:
            return False

        if value == currentNode.value:
            return True

        if value < currentNode.value:
            return self.__rContains(currentNode.left, value)

        if value > currentNode.value:
            return self.__rContains(currentNode.right, value)

    def rInsert(self, value):
        if self.root == None:
            self.root = self.__rInsert(self.root, value)

        self.__rInsert(self.root, value)

    def __rInsert(self, currentNode, value):
        if currentNode == None:
            return Node(value)

        if value < currentNode.value:
            currentNode.left = self.__rInsert(currentNode.left, value)

        if value > currentNode.value:
            currentNode.right = self.__rInsert(currentNode.right, value)

        return currentNode

    def deleteNode(self, value):
        self.root = self.__deleteNode(self.root, value)

    def __deleteNode(self, currentNode, value):
        if currentNode == None:
            return None

        if value < currentNode.value:
            currentNode.left = self.__deleteNode(currentNode.left, value)
        elif value > currentNode.value:
            currentNode.right = self.__deleteNode(currentNode.right, value)
        else:
            if currentNode.left == None and currentNode.right == None:
                return None
            elif currentNode.right == None:
                currentNode = currentNode.left
            elif currentNode.left == None:
                currentNode = currentNode.right
            else:
                subTreeMin = self.minValue(currentNode.right)
                currentNode.value = subTreeMin
                currentNode.right = self.__deleteNode(currentNode.right, subTreeMin)

        return currentNode

    def minValue(self, currentNode):
        # if currentNode == None:
        #     return None

        # minimum = self.minValue(currentNode.left)

        # if minimum == None:
        #     minimum = currentNode.value

        # return minimum

        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode.value
