class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def solve(node, max_val):
            if not node:
                return 0
            
            count = 0
            
            if node.val >= max_val:
                count = 1
            
            max_val = max(max_val, node.val)
            
            count += solve(node.left, max_val)
            count += solve(node.right, max_val)
            
            return count
        
        return solve(root, float("-inf"))