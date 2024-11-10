def print_board(board, n):
    print("\nCurrent Board Configuration:")
    print("  " + " ".join([str(i) for i in range(n)]))
    for i in range(n):
        print(f"{i} ", end="")
        for j in range(n):
            if board[i][j] == 1:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()
    print()

def is_safe(board, row, col, n):
    for j in range(n):
        if board[row][j] == 1:
            return False
    
    for i in range(n):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, col, n, first_queen_col):
    if col >= n:
        return True
    
    if col == first_queen_col:
        return solve_n_queens(board, col + 1, n, first_queen_col)
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            
            if solve_n_queens(board, col + 1, n, first_queen_col):
                return True
                
            board[i][col] = 0
    
    return False

def n_queens_interactive():
    while True:
            n = int(input("Enter the size of the board (n x n) : "))
            if n < 4:
                print("Board size must be 4 or greater!")
                continue
            
            while True:
                    print(f"\nEnter the position for the first queen (0 to {n-1}):")
                    first_queen_row = int(input(f"Row (0-{n-1}): "))
                    first_queen_col = int(input(f"Column (0-{n-1}): "))
                    
                    if 0 <= first_queen_row < n and 0 <= first_queen_col < n:
                        break
                    print(f"Please enter valid row and column numbers between 0 and {n-1}")

            
            board = [[0 for x in range(n)] for y in range(n)]
            
            if not is_safe(board, first_queen_row, first_queen_col, n):
                board[first_queen_row][first_queen_col] = 1
            else:
                board[first_queen_row][first_queen_col] = 1
            
            print("\nInitial board with first queen:")
            print_board(board, n)
            
            print("Solving...")
            if solve_n_queens(board, 0, n, first_queen_col):
                print("Solution found!")
                print_board(board, n)
            else:
                print("No solution exists for this configuration.")
            
            again = input("\nWould you like to try another configuration? (yes/no): ").lower()
            if again != 'yes' and again != 'y':
                print("Thank you for using the N-Queens Solver!")
                break

if __name__ == "__main__":
    n_queens_interactive()