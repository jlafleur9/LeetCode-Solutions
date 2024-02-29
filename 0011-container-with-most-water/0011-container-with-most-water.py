class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        
        while left < right:
            currentWater = min(height[left], height[right]) * (right - left)
            if currentWater > maxWater:
                maxWater = currentWater
            if height[left] > height[right]:
                right -= 1
                continue
            else:
                left += 1 
                continue
            if height[left] == height[right]:
                left += 1
                
        return maxWater
                