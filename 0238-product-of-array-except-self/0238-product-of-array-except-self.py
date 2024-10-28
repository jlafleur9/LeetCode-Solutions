class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)
        result = [0] * n
        
        for i in range(0, n):
            result[i] = prefix
            prefix = prefix * nums[i]
            
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * postfix
            postfix = postfix * nums[i]
            
        return result
            
        
        
        
        
#         n = len(nums)
#         right = [1] * n
#         left = [1] * n
        
#         for i in range(1 , n):
#             left[i] = left[i-1] * nums[i - 1]
            
#         for i in range(n - 2, -1, -1):
#             right[i] = right[i + 1] * nums[i + 1]
        
#         result = [left[i] * right[i] for i in range(n)]
        
#         return result