class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        inNums = set()
        
        for num in nums:
            if num in inNums:
                return True
            else:
                inNums.add(num)
                
        return False