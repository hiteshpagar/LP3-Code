class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Maximum value in the knapsack
    for item in items:
        if capacity >= item.weight:
            # If the item can fit entirely in the knapsack
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining capacity
            total_value += item.ratio * capacity
            break
    
    return total_value

# Example usage
if __name__ == "__main__":
    # List of items: (value, weight)
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    
    items = [Item(v, w) for v, w in zip(values, weights)]
    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in Knapsack = {max_value}")
