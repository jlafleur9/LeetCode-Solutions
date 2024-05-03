class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        s1count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        s2count = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for i in range(len(s1)):
            s1count[s1[i]] = 1 + s1count.get(s1[i], 0)
            s2count[s2[i]] = 1 + s2count.get(s2[i], 0)

        matches = 0
        for char in s1count:
            if char in s2count and s1count[char] == s2count[char]:
                matches += 1
                
        left = 0
        
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            char = s2[right]
            s2count[char] += 1
            if s1count[char] == s2count[char]:
                matches += 1
            elif s1count[char] + 1 == s2count[char]:
                matches -= 1
            
            char = s2[left]
            s2count[char] -= 1
            if s1count[char] == s2count[char]:
                matches += 1
            elif s1count[char] - 1 == s2count[char]:
                matches -= 1
                
            left += 1
        
        if matches == 26:
            return True
        return False
        