# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one
# You must a implement a solution with a liner runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num

        return result