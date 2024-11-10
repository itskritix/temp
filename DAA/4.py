def knapsack(items, capacity):
    """
    Solve the 0-1 Knapsack problem using dynamic programming.
    
    Args:
        items: List of tuples (weight, profit) for each item
        capacity: Maximum capacity of the knapsack
    
    Returns:
        tuple: (maximum profit, selected items)
    """
    n = len(items)
    # Create a 2D array to store the maximum profit
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        weight, profit = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + profit)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= items[i - 1][0]
    
    return dp[n][capacity], selected_items

def main():
    try:
        # Get input from user
        n = int(input("Enter number of items: "))
        items = []
        
        # Input validation
        if n <= 0:
            raise ValueError("Number of items must be positive")
        
        # Get weight and profit for each item
        for i in range(n):
            weight = int(input(f"Enter weight of item {i + 1}: "))
            profit = int(input(f"Enter profit of item {i + 1}: "))
            
            if weight <= 0 or profit <= 0:
                raise ValueError("Weight and profit must be positive")
                
            items.append((weight, profit))
        
        capacity = int(input("Enter capacity: "))
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        # Solve the knapsack problem
        max_profit, selected = knapsack(items, capacity)
        
        # Print results
        print("\nResults:")
        print(f"Maximum Profit: {max_profit}")
        print("Selected items (index):", selected)
        print("\nSelected items (weight, profit):")
        for idx in selected:
            print(f"Item {idx + 1}: Weight = {items[idx][0]}, Profit = {items[idx][1]}")
            
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()