"""Smallest subarray """
import math


def smallest_subarray_with_given_sum(s, arr):
    "Smallest subarray funct"
    min_length = math.inf
    window_start, window_sum, min_length = 0, 0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_end >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


# def smallest_subarray_with_given_sum(s, arr):
#     window_start = 0
#     window_sum = 0
#     window_length = math.inf

#     for window_end in range(len(arr)):
#         window_sum += window_end

#         while window_sum >= s:
#             window_length = min(window_length, window_end - window_start + 1)
#             window_sum -= window_start
#             window_start += 1
#         if window_length == math.inf:
#             return 0
#     return window_length

