""" Max Sum Subarray"""
# def max_sum(k, arr):
#    """ Max Sum Func"""
#    max_sum, window_sum, window_start = 0, 0, 0

#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]

#         if window_end >= k -1:
#             max_sum = max(window_sum, max_sum)       
#             window_sum -= arr[window_start]
#             window_start += 1

#     return max_sum


def max_sum(k, arr):
    window_start, window_sum, maxi_sum = 0, 0, 0

    for window_end in range(len(arr)):
        window_sum += window_end

        while window_end > k - 1:
            maxi_sum = max(window_sum, maxi_sum)
            window_sum -= arr[window_start]
            window_start += 1 
        return maxi_sum
