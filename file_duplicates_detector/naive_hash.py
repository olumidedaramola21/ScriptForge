def naive_hash(data):
    return sum(data) % 13


example = bytes("hashing", "utf-8")
print(example)