# LeetCode 76: Minimum Window Substring

# Given 2 strings s and t of lengths m and n, return the minimum window substring of s
# such that every character in t including duplicates is included in window. If no substring found, return empty string

# s = "ADOBECODEBANC" , t = "ABC"
# OUTPUT = "BANC"

# Sliding Window with 2 pointers

from collections import defaultdict

def mws(s,t):
    if len(s) == 0 or len(t) == 0 or len(t) > len(s):
        return ""
    
    t_map = defaultdict(int)

    for elm in t:
        t_map[elm] += 1
    
    required = len(t_map)
    l = 0
    r = 0
    formed = 0

    ans = float("inf"), 0, 0

    window_map = defaultdict(int)

    while r < len(s):

        val = s[r]
        window_map[val] += 1

        if val in t_map and window_map[val] == t_map[val]:
            formed += 1
        
        while ((l <= r) and (formed == required)):
            val_l = s[l]

            if r-l+1 < ans[0]:
                ans = (r-l+1, l, r)
            
            window_map[val_l] -= 1
            if val_l in t_map and window_map[val_l] < t_map[val_l]:
                formed -= 1
            
            l += 1
        
        r += 1
    
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

result = mws("TACOBELL", "CAT")
print(result)