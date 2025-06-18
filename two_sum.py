def two_sum(nums, target):
    seen = {} # A dictionary to store numbers we've seen and their indices
    for i, num in enumerate(nums):  # Loop through list with index
        diff = target - num         # What number do we need to complete the pair?
        if diff in seen:            # If we already saw the number we need:
            return [seen[diff], i]  # Return its index and current index
        seen[num] = i               # Otherwise, store this number and its index
print(two_sum([2, 7, 11, 15], 9))  


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
print(two_sum([3, 8, 12, 4, 7], 11))
    
       