class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        occurrences_map = {}  # Initialize an empty dictionary to store occurrences
        
        for num in nums:
            if num in occurrences_map:
                occurrences_map[num] += 1  # Increment the count if the number is already in the dictionary
            else:
                occurrences_map[num] = 1
            
        unique = 0

        for num in nums:
            if occurrences_map[num] == 1:
                unique += num

        return unique