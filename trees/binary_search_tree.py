import collections


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

    def BFS(self):
        if self.root is None:
            return []

        currentNode = self.root
        queue = []
        results = []

        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)
            results.append(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)

            if currentNode.right is not None:
                queue.append(currentNode.right)

        return results

    def bfsWithLevelDivision(self):
        if self.root is None:
            return []

        result = []

        queue = collections.deque()
        queue.append(self.root)

        while len(queue) > 0:
            queueLength = len(queue)
            level = []

            for i in range(queueLength):
                currentNode = queue.popleft()
                level.append(currentNode.val)

                if currentNode.left is not None:
                    queue.append(currentNode.left)

                if currentNode.right is not None:
                    queue.append(currentNode.right)

            result.append(level)

        return result

    def dfsPreOrder(self):
        results = []

        def traverse(currentNode):
            results.append(currentNode.value)

            if currentNode.left is not None:
                traverse(currentNode.left)

            if currentNode.right is not None:
                traverse(currentNode.right)

        if self.root:
            traverse(self.root)

        return results

    def iterativeDfsPreOrder(self):
        result = []
        stack = []

        currentNode = self.root
        while currentNode or stack:
            if currentNode:
                result.append(currentNode.val)
                stack.append(currentNode.right)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop()

        return result

    def dfsInOrder(self):
        results = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)

            results.append(currentNode.value)

            if currentNode.right is not None:
                traverse(currentNode.right)

        if self.root:
            traverse(self.root)

        return results

    def iterativeDfsInOrder(self):
        result = []
        stackVisitedNodes = []

        currentNode = self.root
        while currentNode or stackVisitedNodes:
            while currentNode:
                stackVisitedNodes.append(currentNode)
                currentNode = currentNode.left

            currentNode = stackVisitedNodes.pop()
            result.append(currentNode.value)
            currentNode = currentNode.right

        return result

    def dfsPostOrder(self):
        results = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)

            if currentNode.right is not None:
                traverse(currentNode.right)

            results.append(currentNode.value)

        if self.root:
            traverse(self.root)

        return results

    def iterativeDfsPostOrder(self):
        stack = [self.root]
        visit = [False]

        result = []

        while stack:
            currentNode, visited = stack.pop(), visit.pop()

            if currentNode:
                if visited:
                    result.append(currentNode.value)
                else:
                    stack.append(currentNode)
                    visit.append(True)

                    stack.append(currentNode.right)
                    visit.append(False)

                    stack.append(currentNode.left)
                    visit.append(False)

        return result

