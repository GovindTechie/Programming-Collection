class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        if root is None or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

def insert_node(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root

def build_bst(values):
    root = None
    for val in values:
        root = insert_node(root, val)
    return root

if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, 12, 18]
    root = build_bst(values)
    val_to_search = 7
    sol = Solution()
    result = sol.searchBST(root, val_to_search)
    if result:
        print("Node found with value:", result.val)
    else:
        print("Value not found")
