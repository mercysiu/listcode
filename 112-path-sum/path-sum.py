# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False 
        target = targetSum - root.val
        if root.left is None and root.right is None:
            if target == 0:
                return True
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
        

        