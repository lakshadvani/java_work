# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
l = []
gluck = 0
def check(l,k):
    for i in l:
        if i<k:
            print(i,k)
            pair = int(k) - int(i)
            if pair in l:
                #print("hit")
                return 
    
        
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        global gluck
        global l
        if(root):
            l.append(root.val)
            self.findTarget(root.left,k)
            self.findTarget(root.right,k)
        for i in l:
            if(i<k):
                    pair = int(k) - int(i)
                    if pair in l:
                        return True
            else:
                    return False
        
        

