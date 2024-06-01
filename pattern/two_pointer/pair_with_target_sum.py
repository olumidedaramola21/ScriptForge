def pair_with_targetsum(arr, target_sum):
    left, right = 0, arr[-1]
    window_sum = 0
    while left < right:
        window_sum = arr[left] + arr[right]
        if window_sum == target_sum:
            return [left, right]
        
        if window_sum > target_sum:
            right -= 1
        else:
            left += 1
    return [-1, -1]
        
