# LeetCode 167: Two Sum II (Input Array is sorted)

# Given a 1 indexed array of integers nums that is already sorted in ascending order,
# find two such numbers that they add up to a specific target number.
# Let these 2 numbers be nums[i1] and nums[i2]
# where 1 <= i1 < i2 <= nums.length

# Return the indices of 2 numbers added by one as an integer array of length 2

# Brute Force (Time Complexity: O(n^2), Space Complexity: O(n))

# def two_sum(arr, target):

#     size = len(arr)
#     if size <= 1:
#         return False
#     else:
#         for i in range(size):
#             for j in range(size):
#                 if i != j and arr[i] + arr[j] == target:
#                     return [i+1, j+1]
    
#     return False

# Better Approach (Time Complexity: O(n), Space Complexity: O(n))
# def two_sum(arr, target):
    
#     rem = dict()

#     for i in range(len(arr)):

#         compliment = target - arr[i]
        
#         if compliment in rem:

#             if i+1 > rem[compliment]+1:
#                 return [rem[compliment] + 1, i+1]
#             else:
#                 return [i+1, rem[compliment] + 1]

#         else:
#             rem[arr[i]] = i

#     return False

# Best Approach (Time Complexity: O(n), Space Complexity: O(1))

def two_sum(arr, target):
    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[l] + arr[r] > target:
            r -= 1

        elif arr[l] + arr[r] < target:
            l += 1
        
        else:
            return [l+1, r+1]
    
    return False

result = two_sum([2,5,6,8,10,12,21,42], 11)
print(result)