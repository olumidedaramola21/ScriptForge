"""Medium """
from re import L
from numpy import left_shift


def fruits_into_baskets(fruits):
  """ Basket funct"""
    max_length = 0
    window_start = 0
    char_freq = {}
  
    for window_end in range(len(fruits)):
        right_str = fruits[window_end]
        if right_str not in char_freq:
           char_freq[right_str] = 0
        char_freq[right_str] += 1

        while len(char_freq) >  2:
            left_shift = fruits[window_start]
            char_freq[left_shift] -= 1
            if char_freq[left_shift] == 0:
               del char_freq[left_shift]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

  return max_length
