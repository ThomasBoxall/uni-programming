class Hash:
    def __init__(self):
        self.size = 10
        #A prime number is normally used like 53, 97, 193, 389, 769, 1543, 3079 ...
        self.hashTable = []
        for i in range(self.size):
            self.hashTable.append([])

    def hashFun(self, key):
        #Here we use a different hash function
        code = key
        for i in range (len(str(key))):
            code = 17 * code + ord(str(key)[i])
        return code % len(self.hashTable)
    
    def search(self, key):
        address = self.hashFun(key)
        start = address
        #Chaining
        for i in range (len(self.hashTable[address])):
            if (self.hashTable[address][i][0] == key):
                print("The item is found, key is " + str(key) + " and datais"+str(self.hashTable[address][i][1]) + " which is stored at the"+str(address) + "-th entry of the hashtable")
                return address
        print("Not found")
        return -1

    def insert(self, key, newData):
        elements = [key, newData]
        start = self.hashFun(key)
        address = start
        #Chaining
        self.hashTable[address].append(elements)

    def delete(self, key):
        address = self.hashFun(key)
        start = address
        #Chaining
        for i in range(len(self.hashTable[address])):
            if (self.hashTable[address][i][0] == key):
                print("The item is found and deleted, key is " + str(key) +" anddata is " + str(self.hashTable[address][i][1]) + " which is stored at the"+str(address) + "-th entry of the hashtable and " + str(i) + "-th nodeinthelist")
                self.hashTable[address].pop(i)
                return
        print("Not found")

myhash1 = Hash()
myhash1.insert(10, "\'zhoudalin\''")
myhash1.search(10)
myhash1.search(15)
myhash1.insert(20, "\'dsalg\'")
myhash1.search(20)
myhash1.insert(40, "\'dsalg2\'")
myhash1.search(40)
myhash1.insert(0, "\'one more thing\'")
myhash1.search(0)
myhash1.insert(3, "\'9999999\'")
myhash1.search(3)
myhash1.insert(50, "\'Another collision\'")
myhash1.search(50)
myhash1.insert(13, "\'Last collision\'")
myhash1.search(13)
myhash1.delete(13)
myhash1.search(13)
myhash1.delete(1)
myhash1.insert(13, "\'Last collision\'")
myhash1.search(13)