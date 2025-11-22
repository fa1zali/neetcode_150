# LeetCode 424: Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other 
# uppercase English character. You can perform this operation at most k times.

# Return the length of longest substring containing the same letter you can get after performing the above operations.

# s = "ABAB", k=2
# Output = 4 (Replace 2 A's with 2 B's or vice versa)

from collections import defaultdict

def lrcr(s,k):

    left = 0
    max_freq = 0
    max_length = 0

    counts = defaultdict(int)

    for right in range(len(s)):

        # Expand window
        counts[s[right]] += 1
        max_freq = max(max_freq, counts[s[right]])

        # check window length

        window_length = right - left + 1

        if window_length - max_freq > k:
            counts[s[left]] -= 1

            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

result = lrcr("ABAB", 2)
print(result)