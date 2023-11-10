def shortestPathLength(graph):
    n = len(graph)
    target_mask = (1 << n) - 1  # All nodes visited

    # Create a memoization table to store the shortest path lengths
    memo = [[float('inf')] * (1 << n) for _ in range(n)]

    # Queue to perform Breadth-First Search
    queue = [(i, 1 << i, 0) for i in range(n)]

    # Initialize memo table for starting nodes
    for i in range(n):
        memo[i][1 << i] = 0

    while queue:
        current, mask, cost = queue.pop(0)

        # If all nodes are visited, return the shortest path
        if mask == target_mask:
            return cost

        for neighbor in graph[current]:
            new_mask = mask | (1 << neighbor)

            # If the new state has a shorter path, update the memo table and enqueue the new state
            if cost + 1 < memo[neighbor][new_mask]:
                memo[neighbor][new_mask] = cost + 1
                queue.append((neighbor, new_mask, cost + 1))

    return -1  # It should never reach here for a connected graph

# Example 1
graph1 = [[1, 2, 3], [0], [0], [0]]
print(shortestPathLength(graph1))  # Output: 4

# Example 2
graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]
print(shortestPathLength(graph2))  # Output: 4
