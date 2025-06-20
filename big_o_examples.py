
# File: big_o_examples.py
# Description: Demonstrates examples of different time complexities — O(1), O(n), and O(n^2).

def constant_time():
    """
    Demonstrates O(1) constant time complexity.
    Performs a simple fixed-time operation.
    """
    x = 5 + 10
    print("Constant time:", x)

# O(n)
def linear_time(arr):
    """
    Demonstrates O(n) linear time complexity.
    
    Parameters:
    arr (list): List of elements to iterate over.
    """
    print("Linear time:")
    for i in arr:
        print(i)

# O(n^2)
def quadratic_time(arr):
     """
    Demonstrates O(n^2) quadratic time complexity using nested loops.
    
    Parameters:
    arr (list): List of elements to compare in pairs.
    """
    print("Quadratic time:")
    print("Quadratic time:")
    for i in arr:
        for j in arr:
            print(i, j)
# Example usage
constant_time()
linear_time([1, 2, 3])
quadratic_time([1, 2, 3])
