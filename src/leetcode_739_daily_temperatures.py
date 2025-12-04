# LeetCode 739: Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait
# after the ith day to get warmer temperature. If there is no future day for which this is possible
# keep answer[i] == 0 instead.

# temperature = [73, 74, 75, 71, 69, 72, 76, 73]
# answer = [1,1,4,2,1,1,0,0]

# Brute Force (Time Complexity: O(n^2), Space Complexity: O(n))
# def dt(temperature):
    
#     n = len(temperature)
#     answer = [0]*n

#     for i in range(n-1):
#         for j in range(i+1,n):

#             if temperature[j] > temperature[i]:
#                 answer[i] = j-i
#                 break
    
#     return answer

# Optimized approach (Time Complexity: O(n), Space Complexity: O(n))
def dt(temperature):
    
    n = len(temperature)
    answer = [0] * n
    index_stack = []

    for i in range(n):
        while len(index_stack) != 0 and temperature[i] > temperature[index_stack[-1]]:
            index = index_stack.pop()
            answer[index] = i - index
        
        index_stack.append(i)
    
    return answer

result = dt(temperature = [73, 74, 75, 71, 69, 72, 76, 73])
print(result)