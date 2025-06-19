# File: array_basics.py
# Description: Demonstrates basic array operations in Python such as iteration, indexing, and slicing.

arr = [1,2,3,4,5]
print("third element:", arr[2])
arr.append(9)
print("after appending:" , arr)
arr.remove(2)
print("after removing 2:", arr)
print("all elements:")
for num in arr:
    print(num)

