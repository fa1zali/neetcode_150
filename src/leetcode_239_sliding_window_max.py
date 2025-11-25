# LeetCode 239: Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k, which is
# moving from the very left to the very right. You can only see k numbers in the window.
# Each time the slide moves to the right by one position.

# Return max sliding window.

# Brute Force (Time Complexity: O(n^2), Space Complexity: O(n))
# def swm(nums, k):

#     n = len(nums)
#     arr = []
    
#     for i in range(n):
#         if k + i <= n:
#             arr.append(max(nums[i:k+i]))
    
#     return arr

from collections import deque

def swm(nums, k):

    if not nums or k <= 0:
        return []
    
    n = len(nums)

    if k > n:
        return [max(nums)]

    maximum = []
    dq = deque()

    for i in range(n):
        if dq and dq[0] == i-k:
            dq.popleft()
        
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)

        if i >= k-1:
            maximum.append(nums[dq[0]])

    return maximum

result = swm([1,2,3,4,5,6,7,8,9], 3)
# result = swm([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)