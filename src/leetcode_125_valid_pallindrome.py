# LeetCode 125: Valid Palindrome

# A phrase is a pallindrome if after converting all uppercase letters to lowercase letters
# and removing all non alpha numeric characters, it reads same forward and backward.

# Input: Race a Car
# Result: False
# Explanation: raceacar != racaecar

# Time Complexity: O(n), Space Complexity: O(n)

# def valid_pallindrome(str):
#     upd_str = ""
#     rev_str = ""
#     for elm in str:
#         if elm.isalnum():
#             upd_str += elm.lower()

#     for i in range(len(upd_str)-1, -1, -1):
#         rev_str += upd_str[i]
    
#     if upd_str == rev_str:
#         return True
    
#     return False


def valid_pallindrome(str):
    l = 0
    r = len(str) - 1

    while l < r:
        
        while (l<r and not str[l].isalnum()):
            l += 1
        
        while (l<r and not str[r].isalnum()):
            r -= 1
        
        if str[l].lower() != str[r].lower():
            return False
        
        l += 1
        r -= 1
    
    return True

# result = valid_pallindrome("Race a Car")
result = valid_pallindrome("ma d am")
print(result)