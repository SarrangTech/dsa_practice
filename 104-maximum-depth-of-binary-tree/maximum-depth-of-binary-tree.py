
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root,counter=0):
        if root is None:
            return counter
        left=self.maxDepth(root.left,counter+1)
        right=self.maxDepth(root.right,counter+1)
        return max(left,right)
        