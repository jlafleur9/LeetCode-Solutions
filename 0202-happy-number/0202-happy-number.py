class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
            
        while n not in cycle:
            cycle.add(n)
            digits = str(n)
            n = sum(int(digit)**2 for digit in digits)
            if n == 1:
                return True
        
        return False
            
            
            