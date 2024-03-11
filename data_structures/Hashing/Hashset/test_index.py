from index import MyHashSet
import unittest

class TestMyHashSet(unittest.TestCase):
    def test_add(self):
        #create a hashset with capacity of 5
        hash_set = MyHashSet(5)

        # Add some elements
        hash_set.add(1)
        hash_set.add(2)
        hash_set.add(3)

        # Assert that the elements have been added 
        self.assertIn(1, hash_set.buckets[hash_set._hash(1)])
        self.assertIn(2, hash_set.buckets[hash_set._hash(2)])
        self.assertIn(3, hash_set.buckets[hash_set._hash(3)])

        # Remove an element
        hash_set.remove(2)

        # Assert that the element has been removed
        self.assertNotIn(2, hash_set.buckets[hash_set._hash(2)])

        # Assert that hashset contains the element
        self.assertTrue(1, hash_set.buckets[hash_set._hash(1)]) 





if __name__ == '__main__':
    unittest.main