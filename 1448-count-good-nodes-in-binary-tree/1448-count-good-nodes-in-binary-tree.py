# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        value = 0
        
        if not root:
            return None

        maxVal = root.val
        
        def dfs(root, maxVal):
            nonlocal value
            if not root:
                return None
            if root.val >= maxVal:
                value += 1
                maxVal = max(maxVal, root.val)
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        
        dfs(root, maxVal)
        return value
        