# Top K Frequent elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return answer in any order
# nums = [1,1,1,2,2,3], k=2
# [1,2]

# Brute Force - Sorting 

# def top_k(nums, k):

#     nums.sort()

#     val = dict()
#     freq = []

#     for elm in nums:
#         val[elm]= val.get(elm, 0) + 1
    
#     i = 0
#     for key in val.keys():
#         if i < k:
#             freq.append(key)
#             i += 1
#     return freq

# print(top_k([2,1,1,1,2,3], 2))

# Optimized approach using heaps

import heapq

def top_k(nums, k):

    heap = []
    map = dict()
    freq = []

    if len(nums) == k:
         return nums

    for elm in nums:
        map[elm]= map.get(elm, 0) + 1

    for key,val in map.items():
            heapq.heappush(heap, (val, key))
    
    if len(heap) > k:
        pop = len(heap) - k
    
        for i in range(pop):
            heapq.heappop(heap)

    for elm in heap:
        freq.append(elm[1])
    
    return freq

print(top_k([2,1,1,1,2,3], 2))