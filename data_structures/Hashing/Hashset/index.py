# Implementation of a basic Hashset
class MyHashSet:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * self.capacity
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def add(self, key):
        index = self._hash(key)
        
        if not self.buckets[index]:
            self.buckets[index] = []
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key): 
        index = self._hash(key)
        if self.buckets[index] and key in self.buckets[index ]:
            self.buckets[index].remove(key)

    def contains(self, key): 
        index = self._hash(key)
        return self.buckets[index] and key in self.buckets[index ]
    
obj = MyHashSet()
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)


