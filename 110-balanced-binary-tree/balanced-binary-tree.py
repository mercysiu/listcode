# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def isBalanced(self, root):
#         if not root or (not root.left and not root.right):
#             return True
#         def count_turns(root):
#             if root is None:
#                 return 0, 0
#             left_a, left_b = 0, 0
#             right_a, right_b = 0, 0
#             if root.left:
#                 la, lb = count_turns(root.left)
#                 left_a, left_b = la + 1, lb
#             if root.right:
#                 ra, rb = count_turns(root.right)
#                 right_a, right_b = ra, rb + 1
#             return left_a + right_a, left_b + right_b
#         l, r = count_turns(root)
#         if l == 0:
#             if r == 1:
#                 return True
#             else:
#                 return False
#         if r == 0:
#             if l == 1:
#                 return True
#             else:
#                 return False

#         def minDepth(root):
#             if not root:
#                 return 0
#             if not root.left and root.right:
#                 return 1 + minDepth(root.right)
#             if not root.right and root.left:
#                 return 1 + minDepth(root.left)
#             return 1 + min(minDepth(root.left), minDepth(root.right))
#         def maxDepth(root):
#             if not root:
#                 return 0
#             return 1 + max(maxDepth(root.left), maxDepth(root.right))
#         maxdepth = maxDepth(root)
#         mindepth = minDepth(root)
#         neg = maxdepth - mindepth
#         if neg  >= 2:
#             return False
#         return True 
#dfs di xuong ben duoi node la duyet len tren
#qua moi node kiem tra do dai cua nhanh trai nhanh phai
#lay -1 lam he so can bang
#neu chenh lech nhanh trai va phai o moi node > 1
#node do se tra ve -1(hoac bat ki ki hieu rieng nao) 
#gia tri se duoc mang len toi root de ham tra ve -1
#khi goi ham kiem tra gia tri ham tra ve de xac dinh cay can bang
class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0             
            left = check(node.left)

            if left == -1: return -1 
            
            right = check(node.right)

            if right == -1: return -1 
           
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return check(root) != -1
        