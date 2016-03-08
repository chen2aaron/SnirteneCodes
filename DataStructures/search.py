import random


def sequential_search(data, target):
    position = 0
    found = False
    while position < len(data) and not found:
        if data[position] == target:
            found = True
        else:
            position += 1
    return found, position


def binary_search(data, target):
    first = 0
    last = len(data) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if data[midpoint] == target:
            found = True
        else:
            if target < data[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found, first, last


def random_list():
    x = random.randint(1, 10)
    result = []
    for i in range(20):
        result.append(x + random.randint(1, 10))
        x += random.randint(1, 10)
    return result


class HashTable(object):
    """
    remainder method
    """

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put_data_in_slots(self, key, data, slot):
        if self.slots[slot] == None:
            self.slots[slot] = key
            self.data[slot] = data
            return True
        else:
            if self.slots[slot] == key:  # not None
                self.data[slot] = data  # replace
                return True
            else:
                return False

    def put(self, key, data):
        slot = self.hash(key, self.size)
        result = self.put_data_in_slots(key, data, slot)
        while not result:
            slot = self.rehash(slot, self.size)
            result = self.put_data_in_slots(key, data, slot)

    def hash(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


class OtherHashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                                self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)


if __name__ == '__main__':
    data = random_list()
    print(data)
    print(sequential_search(data, 22))
    print(binary_search(data, 22))

    table = HashTable()
    print(table.size)
    table[54] = 'cat'
    table[26] = 'dog'
    table[93] = 'lion'
    table[17] = "tiger"
    table[77] = "bird"
    table[44] = "goat"
    table[55] = "pig"
    table[20] = "chicken"
    print(table.slots)
    print(table.data)
