import sys
import glob


def same_bytes(left_name, right_name):
    left_bytes = open(left_name, "rb").read()
    right_bytes = open(right_name, "rb").read()
    return left_bytes == right_bytes

def find_duplicates(filenames):
    matches = []
    for i, left in enumerate(filenames):
        for right in filenames[i + 1:]:
            if same_bytes(left, right):
                matches.append((left, right))
    return matches

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brute_force.py <pattern>")
        sys.exit(1)

    pattern = sys.argv[1]
    filenames = glob.glob(pattern)
    
    if not filenames:
        print(f"No files found matching the pattern: {pattern}")
        sys.exit(1)

    duplicates = find_duplicates(filenames)
    for (left, right) in duplicates:
        print(left, right)
