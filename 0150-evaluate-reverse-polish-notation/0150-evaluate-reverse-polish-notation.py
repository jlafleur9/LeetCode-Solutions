class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for item in tokens:
            if item == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
                continue
            if item == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
                continue
            if item == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
                continue
            if item == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
                continue
            stack.append(int(item))
        
        return stack[0]
        
            