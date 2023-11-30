def naive_hash(data):
    return sum(data) % 13


# Here is a quick test that calculates the hash code for successively longer substrings of the word "hashing":

example = bytes("    3 May. Bistritz.—Left Munich at 8:35 P. M., on 1st May, arriving at Vienna early next morning; should have arrived at 6:46, but train was an hour late. Buda-Pesth seems a wonderful place, from the glimpse which I got of it from the train and the little I could walk through the streets. I feared to go very far from the station, as we had arrived late and would start as near the correct time as possible. The impression I had was that we were leaving the West and entering the East; the most western of splendid bridges over the Danube, which is here of noble width and depth, took us among the traditions of Turkish rule    ", "utf-8")
for i in range(1, len(example) + 1):
    substring = example[:i]
    hash = naive_hash(substring)
    print(f"{hash:2} {substring}")