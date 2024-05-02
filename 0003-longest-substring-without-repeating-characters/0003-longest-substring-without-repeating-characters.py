class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        substring = set()
        left = 0
        
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
                    
            substring.add(s[right])
            length = max(length, right - left + 1)
            
        return length