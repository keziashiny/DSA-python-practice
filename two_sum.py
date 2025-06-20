# File: two_sum.py
# Description: Solves the Two Sum problem using a dictionary (hash map) for efficient lookup.

def two_sum(nums, target):
    """
    Finds indices of two numbers in 'nums' that add up to 'target'.

    Parameters:
    nums (list): List of integers.
    target (int): Target sum to find.

    Returns:
    list: Indices of the two numbers that add up to target.
    """
    seen = {}  # Dictionary to store numbers and their indices
    
    for i, num in enumerate(nums):
        diff = target - num  # Number needed to reach the target sum
        
        if diff in seen:
            return [seen[diff], i]  # Return indices if pair found
        
        seen[num] = i  # Store the current number with its index

# Example usage
print(two_sum([2, 7, 11, 15], 9))   # Output: [0, 1]

def two_sum(nums, target):
    """
    Another implementation of Two Sum with the same logic.
    """
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Example usage
print(two_sum([3, 8, 12, 4, 7], 11))  # Output: [1, 4]

       
