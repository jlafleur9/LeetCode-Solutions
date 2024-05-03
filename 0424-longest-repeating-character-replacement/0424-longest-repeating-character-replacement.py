class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left, right = 0, 0
        
        maxFrequency = 0
        
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxFrequency = max(maxFrequency, count[s[right]])
            
            while(right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            right += 1
        
        return result