"""Hash Map - Usage """
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
# both key and value can have different type in a hashmap
hashmap["pi"] = 3.1415
print(hashmap)
# get the size of the hashmap
print("the size of the hashmap is: " + str(len(hashmap)))
# iterate the hashmap
for key in hashmap:
    print("(" +  str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("are in the hashmap")
# Get all the keys
print(hashmap.keys())
# Clear the hash map
hashmap.clear()
print("The size of hash map is " + str(len(hashmap)))
