# LeetCode 42: Trapping rain water

# Given n non negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining

# height = [0,1,0,2,1,0,1,3,2,1,2,1] >> 6

# Brute Force (Time Complexity: O(n), Space Complexity: O(n))
# def rain_water(height):
#     n = len(height)
#     left_max = []
#     right_max = [0 for i in range(n)]
#     left_max_val = 0
#     right_max_val = 0
#     total = 0

#     for i in range(n):
#         if height[i] > left_max_val:
#             left_max_val = height[i]
#         left_max.append(left_max_val)

#     for j in range(n-1, -1, -1):
#         if height[j] > right_max_val:
#             right_max_val = height[j]
#         right_max[j] = right_max_val
    
#     for k in range(n):

#         if min(left_max[k], right_max[k]) - height[k] > 0:
#             total = total + min(left_max[k], right_max[k]) - height[k]
    
#     return total

# Two Pointer Approach (Time Complexity: O(n), Space Complexity: O(1))
def rain_water(height):
    left = 0
    right = len(height) - 1
    total = 0

    left_max = height[0]
    right_max = height[len(height)-1]

    while left < right:

        if height[left] < height[right]:
            left_max = max(left_max, height[left])

            if left_max - height[left] > 0:
                total = total + left_max - height[left]

            left += 1
        else:
            right_max = max(right_max, height[right])

            if right_max - height[right] > 0:
                total = total + right_max - height[right]
            
            right -= 1
    
    return total

result = rain_water([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)