# Given an integer array nums, return True if any value appears twice in the array, and return False if every element is distinct.
# nums = [1,4,3,5,4] >> True

# Brute Force (O n^2)

# def check_duplicates(nums: list):
#     if len(nums) < 2:
#         return False
#     else:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] == nums[j] and i != j:
#                     return True
    
#     return False

# print(check_duplicates([1,4,3,5,4]))
# print(check_duplicates([1,2,3,5,4]))

# Optimized Approach

# 1. Sorting and then checking in pairs (O n log_n)
# 2. Using Data Structures like set (O n)

def check_duplicates(nums: list):
    if len(nums) < 2:
        return False
    else:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] not in nums_set:
                nums_set.add(nums[i])
            else:
                return True
    
    return False

print(check_duplicates([1,4,3,5,4]))
print(check_duplicates([1,2,3,5,4]))