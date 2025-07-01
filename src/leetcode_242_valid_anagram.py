# Given 2 strigs s and t, return True if t is an anagram of s and false otherwise
# s = cat and t = tac --> True

# Brute Force

def valid_anagram(s, t):

    count_s = dict()
    count_t = dict()

    if len(s) != len(t):
        return False
    else:
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
        
# print(valid_anagram("aaaaabb", "cccbbbb"))
# print(valid_anagram("cat", "tac"))
# print(valid_anagram("sam", "sat"))

# Optimized Approach

# Using array O(n)

def valid_anagram(s, t):

    if len(s) != len(t):
        return False
    else:
        arr = [0 for i in range(26)]

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1
        
        print(arr)
        
    for elm in arr:
        if elm != 0:
            return False
    
    return True

# print(valid_anagram("aaaaabb", "cccbbbb"))
# print(valid_anagram("cat", "tac"))
# print(valid_anagram("sam", "sat"))
