from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # Sort each string to get its canonical representation
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return list(anagrams.values())