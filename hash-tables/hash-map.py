class HashMap:
    def __init__(self, size: int = 7) -> None:
        self.hashMap = [None] * size

    def __hash(self, key: str):
        myHash = 0
        for letter in key:
            myHash = (myHash + ord(letter) * 23) % len(self.hashMap)

        return myHash

    def setItem(self, key: str, value: int) -> None:
        index = self.__hash(key)

        if self.hashMap[index] == None:
            self.hashMap[index] = []

        for i, pair in enumerate(self.hashMap[index]):
            recordKey, recordValue = pair

            if recordKey == key:
                self.hashMap[index][i] = [key, value]
                return

        self.hashMap[index].append([key, value])

    def getItem(self, key: str) -> int:
        index = self.__hash(key)

        if self.hashMap[index] is not None:
            for pair in self.hashMap[index]:
                recordKey, recordValue = pair

                if recordKey == key:
                    return recordValue

        return None

    def removeItem(self, key: str) -> None:
        index = self.__hash(key)

        if self.hashMap[index] is not None:
            for i, pair in enumerate(self.hashMap[index]):
                recordKey, recordValue = pair

                if recordKey == key:
                    del self.hashMap[index][i]
                    return

    def getKeys(self) -> list:
        keys = []

        for bucket in self.hashMap:
            if bucket is not None:
                for pair in bucket:
                    recordKey, recordValue = pair
                    keys.append(recordKey)

        return keys

    def __str__(self):
        mapStr = "{"

        isEmpty = True
        for bucket in self.hashMap:
            if bucket is not None:
                for pair in bucket:
                    isEmpty = False
                    key, value = pair
                    mapStr += key + ": " + str(value) + ", "

        if isEmpty:
            mapStr += "}"
        else:
            mapStr = mapStr[0:-2] + "}"

        return mapStr

