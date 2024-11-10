# Write a program to solve a fractional Knapsack problem using a greedy method.

def get_profit_weight_ratio(item):
    weight, profit = item
    return profit / weight

def fractional_knapsack(items, capacity):
    items.sort(key=get_profit_weight_ratio, reverse=True)
    total_profit = 0

    for weight, profit in items:
        if capacity >= weight:
            total_profit += profit
            capacity -= weight
        else:
            total_profit += profit * (capacity / weight)
            break  

    return total_profit

n = int(input("Enter number of items: "))
items = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    profit = int(input(f"Enter profit of item {i + 1}: "))
    items.append((weight, profit))

capacity = int(input("Enter knapsack capacity: "))

max_profit = fractional_knapsack(items, capacity)
print("Maximum Profit:", max_profit)























# def print_items(items):
#     print("-----------")
#     print(" W  P  P/W")
#     for item in items:
#         weight, profit, pw_ratio = item
#         print(str(weight) + "  " + str(profit) + "  " + "{:.2f}".format(pw_ratio))
#     print("-----------")

# print("\nItems before sorting:")
# print_items(items)