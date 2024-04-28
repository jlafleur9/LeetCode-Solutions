class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        
        if len(s) != len(t):
            return False
        
        
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        
        for char in t:
            if char in char_map and char_map[char] != 0:
                char_map[char] -= 1
            else:
                return False
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        char_map2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        
        for char in t:
            if char in char_map and char_map[char] !=0:
                char_map[char] -= 1
            else:
                return False
        return True