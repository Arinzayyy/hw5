def lexicalOrder(n):
    result = []

    def dfs(current):
        if current > n:
            return

        result.append(current)
        dfs(current * 10)  # Explore the subtree rooted at current*10
        if current % 10 < 9:
            dfs(current + 1)  # Move to the next sibling within the same level

    dfs(1)  # Start the DFS from 1
    return result

# Example 1
print(lexicalOrder(13))  # Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

# Example 2
print(lexicalOrder(2))   # Output: [1,2]
