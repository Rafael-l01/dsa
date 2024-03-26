class DynamicArray:
    def __init__(self, capacity: int):
        if capacity < 0:
            raise Exception("Array capacity needs to be bigger or equals than 0")

        if capacity == 0:
            self.array = []
        else:
            self.array = [0] * capacity

        self.capacity = capacity
        self.size = 0

    def isPositionValid(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")

    def get(self, index: int) -> int:
        self.isPositionValid(index)

        return self.array[index]

    def set(self, index: int, value: int) -> None:
        self.isPositionValid(index)

        self.array[index] = value

    def pushback(self, value: int) -> None:
        if self.size == self.capacity:
            self.grow()

        self.array[self.size] = value
        self.size += 1

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            raise Exception("Index out of bounds")

        if self.size == self.capacity:
            self.grow()

        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise Exception("Pop from empty list")

        last_position = self.size - 1
        value = self.array[last_position]

        self.array[last_position] = 0
        self.size -= 1

        return value

    def delete(self, index: int) -> int:
        if self.size == 0:
            raise Exception("Pop from empty list")

        self.isPositionValid(index)

        value = self.array[index]

        last_position = self.size - 1
        for i in range(index, last_position):
            self.array[i] = self.array[i + 1]

        self.array[last_position] = 0
        self.size -= 1

        if self.size <= int(self.capacity / 2):
            self.shrink()

        return value

    def grow(self) -> None:
        new_capacity = self.capacity * 2

        if new_capacity == 0:
            new_capacity = 10

        new_array = [0] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def shrink(self) -> None:
        new_capacity = int(self.capacity / 2)

        if new_capacity == 0:
            new_array = []

            self.array = new_array
            self.capacity = 0
        else:
            new_array = [0] * new_capacity

            for i in range(self.size):
                new_array[i] = self.array[i]

            self.array = new_array
            self.capacity = new_capacity

    def search(self, value: int) -> int:
        for i in range(self.size):
            if self.array[i] == value:
                return i

        return None

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def isEmpty(self) -> bool:
        return self.size == 0

    def __str__(self) -> str:
        if self.isEmpty():
            return "[]"

        arrayStr = ""
        for i in range(self.size):
            arrayStr += str(self.array[i]) + ", "

        arrayStr = "[" + arrayStr[0:-2] + "]"
        return arrayStr
