# LeetCode 567: Permutation in Strings

# Given two strings s1 and s2, return True if s2 contains a permuation of s1, or False otherwise.

# Sliding Window (Time Complexity: O(n), Space Complexity: O(1))
def ps(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_map = [0] * 26
    s2_map = [0] * 26

    def char_to_index(character):
        return ord(character) - ord('a')

    for i in range(len(s1)):
        s1_map[char_to_index(s1[i])] += 1
        s2_map[char_to_index(s2[i])] += 1

    if s1_map == s2_map:
        return True
    
    for i in range(len(s1), len(s2)):

        s2_map[char_to_index(s2[i])] += 1

        s2_map[char_to_index(s2[i-len(s1)])] -= 1

        if s1_map == s2_map:
            return True
    
    return False

result = ps("abc", "cdxyzbca")
print(result)