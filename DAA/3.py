def get_profit_weight_ratio(item):
    """Calculate profit to weight ratio for an item"""
    weight, profit = item
    return profit / weight

def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack problem using greedy approach
    Args:
        items: List of tuples (weight, profit)
        capacity: Maximum capacity of knapsack
    Returns:
        total_profit: Maximum profit achievable
        selected_items: List of tuples (item_index, fraction_taken)
    """
    # Add index to keep track of original items
    indexed_items = list(enumerate(items))
    
    # Sort items by profit/weight ratio in descending order
    indexed_items.sort(key=lambda x: get_profit_weight_ratio(x[1]), reverse=True)
    
    total_profit = 0
    remaining_capacity = capacity
    selected_items = []

    for index, (weight, profit) in indexed_items:
        if remaining_capacity >= weight:
            # Take whole item
            fraction = 1.0
            total_profit += profit
            remaining_capacity -= weight
        else:
            # Take fractional part of item
            fraction = remaining_capacity / weight
            total_profit += profit * fraction
            remaining_capacity = 0
            
        # Store which items were selected and their fractions
        selected_items.append((index + 1, fraction))
        
        if remaining_capacity == 0:
            break

    return total_profit, selected_items

def main():
    try:
        n = int(input("Enter number of items: "))
        if n <= 0:
            raise ValueError("Number of items should be positive")
            
        items = []
        for i in range(n):
            weight = float(input(f"Enter weight of item {i + 1}: "))
            profit = float(input(f"Enter profit of item {i + 1}: "))
            
            if weight <= 0 or profit < 0:
                raise ValueError("Weight should be positive and profit should be non-negative")
                
            items.append((weight, profit))

        capacity = float(input("Enter knapsack capacity: "))
        if capacity <= 0:
            raise ValueError("Capacity should be positive")

        max_profit, selected_items = fractional_knapsack(items, capacity)
        
        print("\nResults:")
        print(f"Maximum Profit: {max_profit:.2f}")
        print("\nSelected items (Item number, Fraction taken):")
        for item_num, fraction in selected_items:
            print(f"Item {item_num}: {fraction:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()