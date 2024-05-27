"""Finding the sum of all continous subarrays of size k."""

# Bruteforce approach
from curses import window


def find_averages_of_subarray_k(k, arr):
    """Averaging Function"""
    results = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i, k+i):
            _sum+= arr[j]
        results.append(_sum/k)

# Sliding Window approach
# Implementation 1
# def new_find_averages_of_subarray_k(k, arr):
#     """Averaging Function"""
#     results = []
#     window_sum, window_start = 0.0, 0
#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]
#         if window_end >= k -1:
#             results.append(window_sum/k)
#             window_sum -= arr[window_start]
#             window_start += 1
#     return results


# Implementation 2
def new_find_averages_of_subarray_k(k, arr):
    results = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k -1:
            results.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1
    return results


