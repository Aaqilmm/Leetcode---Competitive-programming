# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        k=float("-inf")
        self.first=self.sec=self.prev=None
        current =root
        while current:
            if current.left is None:
                if current.val<k:
                    if not self.first:
                        self.first=self.prev
                    self.second=current
                k=current.val
                self.prev=current
                current=current.right
            else:
                pred=current.left
                while pred.right and pred.right!=current:
                    pred=pred.right
                if pred.right is None:
                    pred.right=current
                    current=current.left
                else:
                    pred.right=None
                    
                    if current.val<k:
                        if not self.first:
                            self.first=self.prev
                        self.second=current
                    k=current.val
                    self.prev=current
                    current=current.right
            
        self.first.val,self.second.val=self.second.val,self.first.val


            
            


            
       
        