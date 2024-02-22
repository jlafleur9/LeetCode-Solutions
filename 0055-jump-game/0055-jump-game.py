class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 2
        count = 0

        if nums[0] == 0 and len(nums) != 1:
            return False

        while right >= 0:
            if nums[right] == 0:
                while nums[right] == 0:
                    right -= 1
                    count +=1
                if nums[right] > count:
                    count = 0
                    right -= 1
                    continue
            if count != 0:
                if nums[right] > count:
                    count = 0
                    right -= 1
                    continue
                else:
                    count += 1
                    right -= 1
                    continue
            right -= 1
            
        

        if count == 0:
            return True
        return False
                
