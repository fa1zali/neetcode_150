# LeetCode 3: Longest Substring Without Repeating Characters

# Given a string s, find the length of longest substring without repeating characters

# s = "abcabcbb"
# Output: 3
# Longest substring without repeating character is "abc"

def longest_substring(s):
    n = len(s)

    if s == None or n == 0:
        return 0
    elif n == 1:
        return 1
    else:

        left = 0
        right = 0
        ans = 0
        
        map = set()

        while right < n:
            if s[right] in map:
                map.remove(s[right])
                left += 1
            
            map.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans

result = longest_substring("abcabcbb")
print(result)