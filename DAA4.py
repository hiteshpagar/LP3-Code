def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP array, where dp[i][w] represents the maximum value for the first i items with a weight limit w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], included_items

# Example usage
weights = [2, 3, 4, 5]  # Weights of the items
values = [3, 4, 5, 6]   # Values of the items
capacity = 5            # Maximum weight capacity of the knapsack

max_value, items = knapsack(weights, values, capacity)
print(f"Maximum value: {max_value}")
print(f"Items included: {items}")
