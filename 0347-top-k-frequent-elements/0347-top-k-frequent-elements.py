class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        frequency = [[] for i in range(len(nums) + 1)]
        
        for num, c in count.items():
            frequency[c].append(num)
        
        result = []
        
        for index in range(len(frequency) -1, 0, -1):
            for num in frequency[index]:
                result.append(num)
                if len(result) == k:
                    return result