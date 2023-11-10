class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    def max_path_sum_helper(node):
        nonlocal max_sum
        if not node:
            return 0

        # Calculate the maximum path sum in the left and right subtrees
        left_sum = max(0, max_path_sum_helper(node.left))
        right_sum = max(0, max_path_sum_helper(node.right))

        # Update the maximum path sum with the current node
        max_sum = max(max_sum, left_sum + right_sum + node.val)

        # Return the maximum path sum that includes the current node
        return max(left_sum, right_sum) + node.val

    # Initialize max_sum to negative infinity
    max_sum = float('-inf')

    # Start the recursive traversal from the root
    max_path_sum_helper(root)

    return max_sum

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(maxPathSum(root1))  # Output: 6

# Example 2
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
print(maxPathSum(root2))  # Output: 42
