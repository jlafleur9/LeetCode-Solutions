class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 
        solution = []
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                solution.append(left + 1)
                solution.append(right + 1)
                return solution
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1