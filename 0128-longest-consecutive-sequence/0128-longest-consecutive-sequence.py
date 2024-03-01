class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        maxSequence = 0
        
        
        for i in nums:
            if (i -1) not in elements:
                isSequence = True
                currentSequence = 1
                while (i + currentSequence) in elements:
                    currentSequence += 1
                maxSequence = max(maxSequence, currentSequence)
        
        return maxSequence
                        