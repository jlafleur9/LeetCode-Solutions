class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for item in tokens:
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(item))
        
        return stack[0]
        
            