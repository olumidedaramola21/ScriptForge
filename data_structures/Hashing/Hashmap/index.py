# Implementation of a basic HashMap

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1 
    
    def remove(self, key): 
        index = self._hash(key)
        prev=None
        current = self.table[index]
        while current:
            if current:
                if current.key == key:
                    if prev is None:
                        self.table[index]= current.next
                    else:
                        prev.next = current.next
                    return
                prev = current
                current = current.next


            
