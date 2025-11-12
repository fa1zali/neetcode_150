# LeetCode 128: Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Write an algorithm which runs in O(n)

# [100,4,200,1,3,2] => 4 ( [1,2,3,4] is the longest sequence )

# Time and Space Complexity (O(n))
def sequence(arr):
    
    # check if we get an empty list
    if len(arr) == 0:
        return False
    
    # to avoid duplicates we will store all integers in a set
    num_set = set()
    lcs = 1

    # adding all integers in set
    for elm in arr:
        num_set.add(elm)
    
    # check if a smaller number exists then current number, then continue
    for elm in num_set:
        if elm - 1 in num_set:
            continue

        current_num = elm
        cs = 1
        while (current_num + 1 in num_set):
            current_num += 1
            cs += 1
        
        lcs = max(lcs, cs)

    return lcs


result = sequence([100,4,200,1,3,2])
print(result)