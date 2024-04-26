class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cat = [] * (2 * len(nums))
        
        for i in range(2):
            for num in nums:
                cat.append(num)
                
        return cat