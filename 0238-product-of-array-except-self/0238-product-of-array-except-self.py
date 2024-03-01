class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1] * n
        left = [1] * n
        
        for i in range(1 , n):
            left[i] = left[i-1] * nums[i - 1]
            
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Multiply the corresponding elements of left and right lists to get the result
        result = [left[i] * right[i] for i in range(n)]
        
        return result