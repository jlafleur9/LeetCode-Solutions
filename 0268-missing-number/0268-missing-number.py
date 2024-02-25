class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        allElements = 0
        
        for i in range(len(nums)):
            allElements += nums[i]
            
        numsSize = len(nums)
        
        total = (numsSize * (numsSize + 1)) // 2
        
        return total - allElements