class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negatives = set()
        largest = 0
        
        for num in nums:
            if num < 0:
                negatives.add(num)
                
        for num in nums:
            if num > 0:
                if -num in negatives:
                    largest = max(largest, num)
                    
        if largest == 0:
            return -1
        
        return largest
                