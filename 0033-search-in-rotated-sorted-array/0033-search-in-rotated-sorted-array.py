class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            
            #determine if our mid is greater than left which means the left half is still sorted. 
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]: #determine either left or right partition
                    left = mid + 1
                else:
                    right = mid - 1
            
            else: # middle is less than left which means pivot is to left of mid
                if target < nums[mid] or target > nums[right]: #determine if target is to left of mid
                    right = mid - 1
                else:
                    left = mid + 1
    
        
        
        return -1
                    