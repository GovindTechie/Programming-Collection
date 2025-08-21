# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution class with level order traversal
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            next_queue = []

            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            result.append(level)
            queue = next_queue

        return result

# ---------- Tree Construction ----------

# Example tree:
#       1
#      / \
#     2   3
#        / \
#       4   5

# Creating nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# ---------- Call Level Order ----------

sol = Solution()
output = sol.levelOrder(root)
print("Level Order Traversal:", output)  # Output: [[1], [2, 3], [4, 5]]
