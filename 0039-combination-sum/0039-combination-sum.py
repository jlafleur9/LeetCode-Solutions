class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        
        def dfs(i):
            if i >= len(candidates):
                return
            if sum(curr) == target:
                result.append(curr.copy())
                return
            if sum(curr) > target:
                return
            
            curr.append(candidates[i])
            dfs(i)
            curr.pop()
            dfs(i + 1)
        
        dfs(0)
        return result
            