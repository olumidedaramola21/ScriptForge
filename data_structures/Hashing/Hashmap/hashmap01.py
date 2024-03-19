# Hash Map - Usage
# The hash map is one of the implementations of a map which is used to store (key, value) pairs.

# init a hash map
hashmap = {0: 0, 2 : 3}
# insert a new (key, value) pair or update the value of existing key
hashmap[1] = 1
hashmap[1] = 4
print(hashmap)
# delete a key
del hashmap[1]
print(hashmap)
# check if a key is in hash map
if 4 not in hashmap:
    print("key 4 not in carrier")

