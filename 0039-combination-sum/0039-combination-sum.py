class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        
        def dfs(i, count):
            if i >= len(candidates):
                return
            if count == target:
                result.append(curr.copy())
                return
            if count > target:
                return
            
            curr.append(candidates[i])
            dfs(i, count + candidates[i])
            curr.pop()
            dfs(i + 1, count)
        
        dfs(0, 0)
        return result
            