class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = [0] * len(height)
        right = [0] * len(height)
        
        maxHeight = 0
        for i in range(len(height)):
            left[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
            
        maxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            right[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
            
        for i in range(len(height)):
            if min(left[i], right[i]) > height[i]:
                water += min(left[i], right[i]) - height[i]
                
        return water
