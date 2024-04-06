class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsMap = {}
        result = set()
        n = len(nums)
        
        for index, value in enumerate(nums):
            numsMap[value] = index
        
        if nums.count(0) == len(nums):
            result.add((0,0,0))
            return result
            
        for i in range(n):
            for j in range(i+1, n):
                target = -nums[i] - nums[j]
                if target in numsMap and numsMap[target] != i and numsMap[target] != j:
                    result.add(tuple(sorted([nums[i], nums[j], target])))

                    
        return result