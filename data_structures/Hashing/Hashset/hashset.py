# A Hashset is one of the implementation of a set which is a data structure to store no repeated value 

# Example of using the Hashset

hashset = set() # init the hashset

hashset.add(3)
hashset.add(4)
hashset.add(5)

hashset.remove(4)

if (3  in hashset):
    print("key found")

print("Size of the hashset:", len(hashset))

for x in hashset:
    print(x, end=" ")

hashset.clear()
print(len(hashset))