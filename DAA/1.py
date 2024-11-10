import time

def recursive_fibonacci(n):
    """
    Calculate nth Fibonacci number recursively
    Time Complexity: O(2^n) - exponential
    Space Complexity: O(n) - due to recursion stack
    """
    if n < 0:
        return "Please enter a positive number"
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def non_recursive_fibonacci(n):
    """
    Calculate nth Fibonacci number iteratively
    Time Complexity: O(n) - linear
    Space Complexity: O(1) - constant
    """
    if n < 0:
        return "Please enter a positive number"
    if n == 0:
        return 0
    
    a, b = 0, 1
    fib_numbers = [a, b]
    
    for i in range(2, n + 1):
        a, b = b, a + b
        fib_numbers.append(b)
    
    return fib_numbers[:n + 1]

def print_sequence(sequence):
    """Helper function to print Fibonacci sequence"""
    for i, num in enumerate(sequence):
        print(f"F({i}) = {num}")

def main():
    while True:
        print("\n=== Fibonacci Sequence Calculator ===")
        print("1. Recursive Method")
        print("2. Non-recursive Method")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            
            if choice == 3:
                print("Goodbye!")
                break
                
            n = int(input("Enter the number of terms (0 or positive): "))
            
            if n < 0:
                print("Please enter a non-negative number")
                continue
                
            if choice == 1:
                print("\nRecursive Fibonacci Sequence:")
                start_time = time.perf_counter()
                
                # Calculate and print each Fibonacci number
                sequence = [recursive_fibonacci(i) for i in range(n)]
                print_sequence(sequence)
                
                end_time = time.perf_counter()
                print(f"\nTime taken: {end_time - start_time:.6f} seconds")
                
            elif choice == 2:
                print("\nNon-recursive Fibonacci Sequence:")
                start_time = time.perf_counter()
                
                # Calculate and print the sequence
                sequence = non_recursive_fibonacci(n)
                print_sequence(sequence)
                
                end_time = time.perf_counter()
                print(f"\nTime taken: {end_time - start_time:.6f} seconds")
                
            else:
                print("Invalid choice! Please enter 1, 2, or 3")
                
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()