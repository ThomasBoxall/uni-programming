import random

def moduloHash(keys, modulus):
    hashTable = [0] * modulus
    for key in keys:
        hashTable[key % modulus] +=1
    return hashTable

keys = random.sample(range(1000), 100)

# print(moduloHash(keys, 10))

modulusValues = [10,20,50,100,200]

for current in modulusValues:
    print(moduloHash(keys, current))