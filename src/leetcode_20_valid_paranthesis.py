# LeetCode 20: Valid Paranthesis

# Given a string s containing just the characters {, }, [, ], (, ) determine if the input string is valid.

# Open brackets should be closed with the same brackets.
# Open Brackets must be closed in the same order.

# s = "{[]}"
# Output= True

# s = "[)]"
# Output=False

# Stack Approach (Time Complexity: O(n), Space Complexity: O(n))
def vp(s):

    stack = []
    map = {")":"(", "}":"{", "]":"["}

    for elm in s:
        if elm in '{[(':
            stack.append(elm)
        
        if elm in '}])' and len(stack) != 0:
            if map[elm] != stack[-1]:
                return False
            else:
                del stack[-1]
        else:
            return False
    
    if len(stack) != 0:
        return False
    
    return True

# result = vp(s = "{[]}")
# result = vp("[)]")
result = vp("])")
print(result)