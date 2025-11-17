# LeetCode 11: Container with most water

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines together with the x-axis form a container, such that the container contains the most water

# Return the maximum amount of water a container can store

# Brute Force (Time Complexity: O(n^2), Space Complexity: O(1))
# def container(arr):
#     n = len(arr)
#     max_water = 0

#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 w = abs(j - i)
#                 h = min(arr[i], arr[j])

#                 content = w*h

#                 if content > max_water:
#                     max_water = content
    
#     return max_water

def container(arr):
    n = len(arr)
    left = 0
    right = n - 1
    max_water = 0

    while left < right:

        width = abs(left-right)
        area = min(arr[left], arr[right]) * width

        max_water = max(max_water, area)

        if arr[left] <= arr[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

result = container([3,2,7,4,1,3,6,2])
print(result)