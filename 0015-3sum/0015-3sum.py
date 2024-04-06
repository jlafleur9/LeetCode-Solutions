class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
                
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                currentValue = value + nums[left] + nums[right]
                if currentValue > 0:
                    right -= 1
                elif currentValue < 0:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    right -= 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
        return result
        