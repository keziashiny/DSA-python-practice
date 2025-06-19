# File: max_sum_subarray.py
# Description: Finds the maximum sum of a subarray of size k using the sliding window technique.

def max_sum_subarray(nums, k):
    """
    Calculates the maximum sum of any contiguous subarray of size k.

    Parameters:
    nums (list): List of integers.
    k (int): Size of the sliding window (subarray length).

    Returns:
    int: Maximum sum of any subarray of size k.
    """
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]

        # Once we reach window size k, slide the window
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1

    return max_sum

# Example usage
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # Output: 9
