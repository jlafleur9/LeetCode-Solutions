class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        
        while left < right:
            tempLeft = s[left]
            tempRight = s[right]
            
            s[left] = s[right]
            s[right] = tempLeft
            
            left += 1
            right -= 1