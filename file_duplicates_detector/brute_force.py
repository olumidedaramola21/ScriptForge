import sys
def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes

def find_duplicates(filename):
    matches = []
    for left in filename:
        for right in filename:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

if __name__ == "__main__":
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)