class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        currentString = ""
        
        def recursive(openP, closedP):
            if openP == closedP == n:
                ans.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                recursive(openP + 1, closedP)
                stack.pop()
            
            if closedP < openP:
                stack.append(")")
                recursive(openP, closedP + 1)
                stack.pop()
                
        recursive(0,0)
        return ans
            
            