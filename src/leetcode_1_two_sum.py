# Given an array of integers nums and an integer target, return indices of 2 numbers such that they add up to the target.
# nums = [1,2,3,5,4] target = 7
# [1,3] or [2, 4]

# Brute Force

# def two_sum(nums, target):

#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j and nums[i] + nums[j] == target:
#                 return i,j
    
#     return False

# print(two_sum([1,2,3,5,4], 7))

# Optimized Approach
# Use data structure Dictionary

def two_sum(nums, target):

    rem = dict()

    for i in range(len(nums)):

        compliment = target - nums[i]

        if compliment in rem:
            return rem[compliment], i
        else:
            rem[nums[i]] = i

    return False

print(two_sum([1,2,3,5,4], 7))