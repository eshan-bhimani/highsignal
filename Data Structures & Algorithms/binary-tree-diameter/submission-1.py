# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 #largest diameter found so far

        def dfs(node):
            nonlocal diameter #share outer diameter variable

            if not node:
                return 0 #empty subtree has height 0
            
            #get heights from children
            left = dfs(node.left)
            right = dfs(node.right)

            # See if the path through THIS node
            # is longer than our previous best
            diameter = max(diameter, left + right)

            # Give parent the height of this subtree
            return 1 + max(left, right)
        
        dfs(root) # Traverse the entire tree
        return diameter # Not dfs(root)'s height


            

