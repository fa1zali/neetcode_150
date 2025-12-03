# LeetCode 22: Generate Paranthsesis

# Given n pairs of paranthesis, write a function to generate all combinations of well formed paranthesis.

# n = 3
#  Output = ["((()))","(()())","(())()","()(())","()()()"]

def generate_paranthesis(n):

    result = []

    def backtrack(s, open, close):
        if len(s) == 2*n:
            result.append(s)
            return
        
        if open < n:
            backtrack(s+'(', open+1, close)
        
        if close < open:
            backtrack(s+')', open, close+1)
    
    backtrack("", 0, 0)

    return result

result = generate_paranthesis(n=2)
print(result)