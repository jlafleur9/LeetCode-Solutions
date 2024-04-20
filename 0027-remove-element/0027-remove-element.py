class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = 0
        k = 0
        
        while right < len(nums):
            if nums[right] == val:
                right += 1
            else:
                nums[k] = nums[right]
                k += 1
                right += 1 
                
        return k
                