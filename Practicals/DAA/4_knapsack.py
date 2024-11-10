#Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy

def knapsack(items, capacity):
    # Create a 2D array to store the maximum profit for each capacity and item combination
    n = len(items)
    dp = [[0] * (capacity + 1) for i in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        weight, profit = items[i - 1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + profit)
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = int(input("Enter weight of item" + str(i + 1)+ ": "))
    profit = int(input(f"Enter profit of item" + str(i + 1)+ ": "))
    items.append((weight, profit))

capacity = int(input("Enter capacity: "))

print("Maximum Profit:", knapsack(items, capacity))

# n=4
# capacity=5
# w1=2
# p1=12

# w2=1
# p2=10

# w3=3
# p3=20

# w4=2
# p4=15