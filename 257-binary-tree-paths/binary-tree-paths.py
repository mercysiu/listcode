# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        if not root: 
            return []
        result = []
        queue = [(root, str(root.val))]
        while queue:
            node, val = queue.pop()
            if not node.left and not node.right:
                result.append(val)
            if node.left:
                queue.append((node.left, val + "->" + str(node.left.val)))
            if node.right:
                queue.append((node.right, val + "->" + str(node.right.val)))
        return result

        
        
                                                                                                               