# Write a program non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity.

import time

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# ---------------------------------------------------------------------------
def non_recursive_fibonacci(n):
    if n <= 0:
        return "Please enter a positive number"
    
    a = 0
    b = 1
    print(f"F(0) = {a}")
    if n == 1:
        return
    print(f"F(1) = {b}")
    
    for i in range(2, n):
        a,b=b,a+b
        print(f"F({i}) = {b}")

# ---------------------------------------------------------------------------

while True:
    print("\n=== Fibonacci Sequence ===")
    print("1. Recursive Method")
    print("2. Non-recursive Method")
    print("3. Exit")
        
    choice = int(input("Enter your choice (1-3): "))
        
    if choice == 3:
        print("Goodbye!")
        break
            
    n = int(input("Enter the number of terms: "))
        
    if n < 0:
        print("Please enter a positive number")
        continue
            
    if choice == 1:
        print("\nRecursive Fibonacci Sequence:")
        start_time = time.perf_counter() 
        for i in range(n):
            print(recursive_fibonacci(i),end=" ")
        end_time = time.perf_counter() 
        print(f"\nTime taken: {end_time - start_time:.6f} seconds")
            
    elif choice == 2:
        print("\nNon-recursive Fibonacci Sequence:")
        start_time = time.perf_counter() 
        non_recursive_fibonacci(n)
        end_time = time.perf_counter() 
        print(f"\nTime taken: {end_time - start_time:.6f} seconds")
            
    else:
        print("Invalid choice! Please enter 1, 2, or 3")
# ---------------------------------------------------------------------------
