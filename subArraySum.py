def subArraySum(arr):
    
    max_sum = current_sum = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_sum += arr[i]
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = arr[i]

    max_sum = max(max_sum, current_sum)
    return max_sum

arr = [10, 20, 30, 5, 20, 40, 50, 10, 20, 30, 40]
print(subArraySum(arr))
