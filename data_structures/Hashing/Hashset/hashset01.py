# Given an array of integers, find if the array contains any duplicates
def find_duplicates(keys):
    hashset = set()
    for key in keys:
        if key in hashset:
            return True
        hashset.add(key)
    return False

# Example Usage
keys = [1, 2, 3, 4, 5, 2, 6, 5, 9, 8]
has_duplicates = find_duplicates(keys)
print(has_duplicates)
