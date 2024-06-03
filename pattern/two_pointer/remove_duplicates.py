def remove_duplicates(arr):

    next_value = 1
    next_non_duplicate = 1
    while next_value < len(arr):
        if arr[next_non_duplicate - 1] != arr[next_value]:
            arr[next_non_duplicate] = arr[next_value]
            next_non_duplicate += 1
        next_value += 1

    return next_non_duplicate












































































