# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# moi lan di xuong thi targetSum giam dan
# den nut la kiem tra dieu kien( thoa thi tra ve True)
# de quy 2 nhanh( dung or de lay duoc ket qua neu 1 nhanh thoa)
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False 
        target = targetSum - root.val
        if root.left is None and root.right is None:
            if target == 0:
                return True
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
        

        