# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, curSum=0) -> bool:
        if not root:
            return False

        curSum += root.val
        if not root.left and not root.right:
            return curSum == targetSum

        return self.hasPathSum(root.left, targetSum, curSum) or self.hasPathSum(root.right, targetSum, curSum)



    