class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        
        for i in range(len(s)):
            char = s[i]
            if not stack:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        result = ''.join(stack)       
        return result