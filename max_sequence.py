def max_sequence(arr):
    if len(arr) == 0:
        return 0
    max_to_date = arr[0]
    current_max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            current_max = arr[i]
        else:
            current_max = current_max + arr[i]
        if max_to_date < current_max:
                max_to_date = current_max
    if max_to_date < 0:
        return 0
    else:
        return max_to_date