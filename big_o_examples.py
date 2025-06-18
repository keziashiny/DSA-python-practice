# O(1)
def constant_time():
    x = 5 + 10
    print("Constant time:", x)

# O(n)
def linear_time(arr):
    print("Linear time:")
    for i in arr:
        print(i)

# O(n^2)
def quadratic_time(arr):
    print("Quadratic time:")
    for i in arr:
        for j in arr:
            print(i, j)

constant_time()
linear_time([1, 2, 3])
quadratic_time([1, 2, 3])
