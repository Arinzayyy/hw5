class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minAbsoluteDifference(root):
    def inorder_traversal(node):
        nonlocal prev, min_diff
        if node is None:
            return

        inorder_traversal(node.left)

        if prev is not None:
            min_diff = min(min_diff, abs(node.val - prev))

        prev = node.val

        inorder_traversal(node.right)

    prev = None
    min_diff = float('inf')

    inorder_traversal(root)

    return min_diff

# Example 1
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

print(minAbsoluteDifference(root1))  # Output: 1

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(48)
root2.right.left = TreeNode(12)
root2.right.right = TreeNode(49)

print(minAbsoluteDifference(root2))  # Output: 1
