class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
                continue
            if not stack:
                return False
            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                    continue
            if c == ']':
                if stack[-1] == '[':
                    stack.pop()
                    continue
            if c == '}':
                if stack[-1] == '{':
                    stack.pop()
                    continue
            return False
                    
        return not stack
                