# Given an array of strings strs, group the anagrams together. You can return answer in any order.

# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the letters exactly once.

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output = [["bat"], ["nat", "tan"], ["eat", "tea", "ate"]]

# sub optimal approach using sorting

# from collections import defaultdict

# def group_anagram(strs):
#     anagrams = defaultdict(list)

#     for word in strs:
#         # Sort the word and use it as a key
#         sorted_word = ''.join(sorted(word))
#         anagrams[sorted_word].append(word)
    
#     print(anagrams)

#     # Return the grouped anagrams as a list of lists
#     return list(anagrams.values())

# print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Optimal approach

def hash(word):
    arr = [0 for i in range(26)]

    for elm in word:
        arr[ord(elm) - ord('a')] += 1
    
    val = ""
    for elm in arr:
        val += str(elm)
    
    return val

def group_anagram(strs):
    anagrams = dict()

    for i in range(len(strs)):

        hash_val = hash(strs[i])

        if hash_val not in anagrams:
            anagrams[hash_val] = [strs[i]]
        else:
            anagrams[hash_val].append(strs[i])
    
    return [v for v in anagrams.values()]

print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))