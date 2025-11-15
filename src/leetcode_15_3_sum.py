# LeetCode 15: 3 Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]],
# such that i!=j, i!=k, j!=k and nums[i] + nums[j] + nums[k] == 0

# Brute Force (Time Complexity: O(n^3) and Space Complexity: O(n))
# def three_sum(nums):

#     ans = []
#     size = len(nums)

#     for i in range(size):
#         for j in range(size):
#             for k in range(size):
#                 if ((i != j) and (i != k) and (j != k)) and ((nums[i] + nums[j] + nums[k]) == 0):
#                     val = sorted([nums[i], nums[j], nums[k]])
#                     if val not in ans:
#                         ans.append(val)
    
#     return ans

# Two Pointer Approach (Time Complexity: O(n^2) and Space Complexity: O(n))
def three_sum(nums):
    
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
            
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif current_sum < 0:
                left += 1
            
            else:
                right -= 1
    
    return result

ans = three_sum([-1,0,1,2,-1,-4])
print(ans)
