# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, leftBoundry, rightBoundry):
            if node is None:
                return True
            
            if not (node.val > leftBoundry and node.val < rightBoundry):
                return False
            
            ## left subtree of node
            return (isValid(node.left, leftBoundry, node.val)
            ## right subtree
            and isValid(node.right, node.val, rightBoundry))


        return isValid(root, float("-inf"), float("inf"))