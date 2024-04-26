class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        
        for item in operations:
            if item == "+":
                stack.append(stack[-1] + stack[-2])                
            elif item == "D":
                stack.append(2 * stack[-1])
            elif item == "C":
                stack.pop()
            else:
                stack.append(int(item))
                
        print(stack)
                
        for num in stack:
            total += num
            
        return total