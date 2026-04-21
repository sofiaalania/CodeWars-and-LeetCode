# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def recurse(node, target):
            if node is None:
                return None

            if target < node.val:
                node.left = recurse(node.left, target)
            elif target > node.val:
                node.right = recurse(node.right, target)
            else:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.val = successor.val
                node.right = recurse(node.right, successor.val)
            return node
        return recurse(root, key)