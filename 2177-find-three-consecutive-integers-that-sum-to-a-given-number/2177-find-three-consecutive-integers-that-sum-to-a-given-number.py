class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        
        
        if num % 3 != 0: 
            no = []
            return no
        else:
            yes = []
            yes.append(num//3 -1)
            yes.append(num//3)
            yes.append(num//3 + 1)
            return yes
            