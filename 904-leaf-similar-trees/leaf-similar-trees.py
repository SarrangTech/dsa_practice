# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
        def leafSimilar(self, root1, root2):

            def getLeaves(root):
                if root is None:
                    return []

                # If this is a leaf, return its value
                if root.left is None and root.right is None:
                    return [root.val]

                # Collect leaves from both subtrees
                left = getLeaves(root.left)
                right = getLeaves(root.right)

                return left + right
            return getLeaves(root1) == getLeaves(root2)

        
        