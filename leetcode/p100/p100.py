# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if not p or not q:
            return False

        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)