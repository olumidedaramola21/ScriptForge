# """ Medium"""
# def longest_substring_with_k_distinct(str, k):
#     window_start = 0
#     max_length = 0
#     char_freg = {}

#     for window_end in range(len(str)):
#         right_str = str[window_end]
#         if right_str not in char_freg:
#             char_freg[right_str] = 0
#         char_freg[right_str] += 1

#         while len(char_freg) > k:
#             left_str = str[window_start]         
#             char_freg[left_str] -= 1
#             if char_freg[left_str] == 0:
#                 del char_freg[left_str]         
#             window_start += 1

#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length


# Another implementation

def longest_substring_with_no_more_than_k_distinct_characters(str, k):
    max_len = 0
    window_start = 0
    char_freq = {}

    for window_end in range(len(str)):
        right_str = str[window_end]
        if right_str not in char_freq:
            char_freq[right_str] = 0
        char_freq[right_str] += 1

        while len(char_freq) > k:
            left_str = str[window_start]
            char_freq[left_str] -= 1
            if char_freq[left_str] == 0:
                del char_freq[left_str]
            window_start += 1
        max_len = max(max_len, window_end - window_start - 1)
        return max_len
