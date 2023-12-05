import glob
import sys
from hashlib import sha256

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    pattern = sys.argv[1]
    print(pattern)
    filenames = glob.glob(pattern)
    print(filenames)
    groups = find_groups(filenames)
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))