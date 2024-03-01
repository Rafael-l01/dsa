class HashSet:
    def __init__(self, size: int = 7):
        self.hashSet = [None] * size

    def __hash(self, value: str):
        myHash = 0
        for letter in value:
            myHash = (myHash + ord(letter) * 23) % len(self.hashSet)

        return myHash

    def addItem(self, value: str) -> None:
        index = self.__hash(value)

        if self.hashSet[index] == None:
            self.hashSet[index] = []

        if self.contains(value):
            return

        self.hashSet[index].append(value)

    def contains(self, value: str) -> bool:
        index = self.__hash(value)

        for recordValue in self.hashSet[index]:
            if recordValue == value:
                return True

        return False

    def removeItem(self, value: str) -> None:
        index = self.__hash(value)

        for i, recordValue in enumerate(self.hashSet[index]):
            if recordValue == value:
                del self.hashSet[index][i]
                return

    def getValues(self) -> list:
        values = []

        for bucket in self.hashSet:
            if bucket is not None:
                for value in bucket:
                    values.append(value)

        return values

    def __str__(self):
        setStr = "{"
        isEmpty = True

        for bucket in self.hashSet:
            if bucket is not None:
                for value in bucket:
                    isEmpty = False
                    setStr += value + ", "

        if isEmpty:
            setStr += "}"
        else:
            setStr = setStr[0:-2] + "}"

        return setStr

