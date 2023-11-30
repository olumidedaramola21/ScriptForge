import sys
import glob


def naive_hash(data):
    return sum(data) % 13

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = naive_hash(data)
        if hash_code not in groups:
            groups[hash_code] = set()
            groups[hash_code].add(fn)
    return groups

def find_duplicates_within_groups(filenames):
    matches = []
    seen_hashes = set()
    for fn in filenames:
        data = open(fn, 'rb').read()
        hash_code = naive_hash(data)
        if hash_code not in seen_hashes:
            seen_hashes.add(hash_code)
        else:
            matches.append(fn)
    return matches

# pattern = sys.argv[1]

# filenames = glob.glob(pattern)
# groups = find_groups(filenames)
# for filenames in groups.values():
#     duplicates = find_duplicates_within_groups(list(filenames))
#     for duplicate in duplicates:
#         print(duplicate)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brute_force.py <pattern>")
        # sys.exit(1)

    
    pattern = sys.argv[1]
    filenames = glob.glob(pattern)
    groups = find_groups(filenames)
    
    if not filenames:
        print(f"No files found matching the pattern: {pattern}")
        # sys.exit(1)

    for filenames in groups.values():
        duplicates = find_duplicates_within_groups(list(filenames))
        for duplicate in duplicates:
            print(duplicate)

   