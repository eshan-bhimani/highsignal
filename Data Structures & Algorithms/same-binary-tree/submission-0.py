# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Base cases go here
        if p == None and q == None:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # Recursively compare left subtrees

        left = self.isSameTree(p.left, q.left)

        # Recursively compare right subtrees
        right = self.isSameTree(p.right, q.right)

        # Return True only if both match
        return left and right
        
       




        