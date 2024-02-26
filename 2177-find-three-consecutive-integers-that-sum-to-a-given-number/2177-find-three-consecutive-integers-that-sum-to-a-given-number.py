class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        no = []
        yes = []
        
        if num % 3 != 0: 
            return no
        else:
            first = num//3 -1
            second = first + 1
            third = second + 1
            
            yes.append(first)
            yes.append(second)
            yes.append(third)
            return yes
            