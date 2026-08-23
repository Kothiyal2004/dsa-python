# Learning the programming in Python 
#Find the smallest number in an array
# Input:
# class Solution:

#     def smallest_number(self, arr):

#         smallest = arr[0]

#         for num in arr:
#             if num < smallest:
#                 smallest = num

#         return smallest


# if __name__ == "__main__":

#     arr = [2, 3, 4, 5, 7, 8, 1]

#     solution = Solution()
#     print(solution.smallest_number(arr))


# To solve this question I m using diff. method to solve it

# 1. Linear Traversal — ⭐ Most Important
arr = [2, 3, 4, 5, 7, 8, 1]

smallest=arr[0]
for num in arr:
    if num<smallest:
        smallest=num
print(smallest)

# Time Complexity : 0(n)
# Space Complexity : 0(1)


# 2. Using Python min() — Built-in Method
arr = [2, 3, 4, 5, 7, 8, 1]

smallest=min(arr)
print(smallest)
# Time: O(n)
# Space: O(1) approximately for the algorithmic idea.

# 3. Sorting

# Sort the array and take the first element:
arr = [2, 3, 4, 5, 7, 8, 1]

arr.sort()
smallest=arr[0]
print(smallest)  #Time: O(n log n)
# Space: depends on the sorting implementation.


#4. use sorted method 
arr = [2, 3, 4, 5, 7, 8, 1]

smallest = sorted(arr)[0]

print(smallest)
# Time: O(n log n)
# Space: O(n)

# . 5. from functools import reduce

from functools import reduce

arr = [2, 3, 4, 5, 7, 8, 1]

smallest = reduce(lambda x, y: x if x < y else y, arr)

print(smallest)