class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1 
        
        while left < right:
            possibleWater = (right - left) * min(height[left], height[right])
            if possibleWater > maxWater:
                maxWater = possibleWater
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxWater