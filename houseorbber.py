# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = []
        even = []
        odd = []
        queue = [[root]]
        while queue:
            level = queue.pop(0)
            temp = []
            new_level = []
            for node in level:
                temp.append(node.val)
            ans.append(temp)
            
            for node in level:
                if(node.left):
                    new_level.append(node.left)
                if(node.right):
                    new_level.append(node.right)
            if(len(new_level)>0):
                queue.append(new_level)
        for i in range(0,len(ans)):
            if(i%2==0):
                even.append(ans[i])
            if(i%2!=0):
                odd.append(ans[i])
        flat_odd = [item for sublist in odd for item in sublist]
        flat_even = [item for sublist in even for item in sublist]
        print(flat_odd,flat_even)
