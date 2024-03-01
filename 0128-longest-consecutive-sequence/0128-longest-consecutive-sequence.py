class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set()
        maxSequence = 1
        currentSequence = 1
        isSequence = True
        
        if not nums:
            return 0
        
        for i in nums:
            elements.add(i)
            
        for i in nums:
            isStart = i -1
            if isStart in elements:
                continue
            else:
                isSequence = True
                while isSequence:
                    i += 1
                    if i in elements:
                        currentSequence += 1
                        if currentSequence > maxSequence:
                            maxSequence = currentSequence
                    else:
                        isSequence = False
                            
                currentSequence = 1
        
        return maxSequence
                        