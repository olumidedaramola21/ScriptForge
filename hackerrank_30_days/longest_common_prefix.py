strs = ["abcd", "abc", "a"]

def longestCommonPrefix(strsList):
    if not strsList:
        return ""
    # we start with the first string as our initial prefix
    prefix = strsList[0]

    for s in strsList[1:]:
               # Keep removing characters from the prefix until it matches the 
        # beginning of the current string
        while s [:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""           
    return prefix
