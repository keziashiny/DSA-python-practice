def max_sum_subarray(nums, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        # Once we hit the window size, start sliding
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1

    return max_sum
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
