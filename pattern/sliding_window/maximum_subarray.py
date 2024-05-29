"""Given an interger array nums, find the subarray with the largest sum, and return its sum """
# nums = [-2, -1, -3, 4, -1, 2, -5, 4]

def find_max_subarray(nums):
    max_sum = nums[0]
    added_sum = 0
    for num in range(len(nums)):
        if added_sum < 0:
            added_sum = 0
        added_sum += num
        max_sum = max(max_sum, added_sum)
    return max_sum
