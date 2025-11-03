# Given an integer array nums, return an answer array such that answer[i] is equal to the product of all the elements of nums except nums[i]

# nums = [1,2,3,4]
# answer = [24, 12, 8, 6]

# Brute Force - Using 2 for loops with complexity O n^2

# def prod_arr(nums):
#     answer = []
    
#     for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod *= nums[j]
#         answer.append(prod)
    
#     return answer

# print(prod_arr(nums = [1,2,3,4]))
# print(prod_arr(nums = [-1,1,0,-3,3]))

# Optimized Approach - Using pre and post variables with complexity of O(n)

def prod_arr(nums):
    size = len(nums)
    answer = [1 for i in range(size)]

    pre = 1
    post = 1

    for i in range(size):
        answer[i] = pre
        pre *= nums[i]

    for j in range(size-1, -1, -1):
        answer[j] = answer[j] * post
        post *= nums[j]

    return answer

print(prod_arr(nums = [1,2,3,4]))

# [1,2,3,4]
# [1,1,2,6]
# [24,12,4,1]