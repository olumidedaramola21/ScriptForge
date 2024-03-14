# # Given an array of integers, find if the array contains any duplicates and return all duplicates found.


def find_duplicates(keys):
    seen = set()
    duplicates = set()
    for key in keys:
        if key in seen:
            duplicates.add(key)
        else:
            seen.add(key)
    return duplicates

# Examle Usage

nums = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 5]
duplicate_numbers = find_duplicates(nums)
print("Duplicates:", duplicate_numbers )