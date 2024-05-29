# """Given an array of positive intergers nums and a positive integer target, return the minimal length of a subabrray whoose sum is greater than or equal to target. if there is no such subarray, return 0 instead """
# nums = [2, 3, 1, 2, 4, 3] target = 7
# nums = [1, 4, 4] target = 4

def find_min_size_subarray(nums, target):
    left_num = 0
    current_sum = 0
    max_lenght = 0

    for right_num in range(len(nums)):
        current_sum += right_num
        if current_sum == target:
            max_lenght = max(max_lenght, right_num - left_num + 1)
            return max_lenght

        while current_sum > target:
            current_sum -= nums[left_num]
            left_num += 1
        
        # max_lenght = max(max_lenght, right_num - left_num + 1)

        return max_lenght
            
