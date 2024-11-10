class NQueens:
    def __init__(self):
        """Initialize the N-Queens solver."""
        try:
            self.size = int(input("Enter size of chessboard: "))
            if self.size <= 3:
                raise ValueError("Board size must be greater than 3 for valid solutions")
            self.board = [[False] * self.size for _ in range(self.size)]
            self.solutions = []
            self.count = 0
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")

    def print_board(self):
        """Print the current state of the board."""
        print("\nCurrent Board Configuration:")
        print("  " + " ".join([str(i + 1) for i in range(self.size)]))  # Column numbers
        for i, row in enumerate(self.board):
            print(f"{i + 1} ", end="")  # Row numbers
            for cell in row:
                print("Q" if cell else ".", end=" ")
            print()
        print()

    def is_safe(self, row: int, col: int) -> bool:
        """
        Check if it's safe to place a queen at the given position.
        
        Args:
            row (int): Row index
            col (int): Column index
            
        Returns:
            bool: True if position is safe, False otherwise
        """
        # Check column (above and below)
        for i in range(self.size):
            if self.board[i][col]:
                return False
        
        # Check diagonal (upper left)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False
                
        # Check diagonal (upper right)
        for i, j in zip(range(row, -1, -1), range(col, self.size)):
            if self.board[i][j]:
                return False
                
        # Check diagonal (lower left)
        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.board[i][j]:
                return False
                
        # Check diagonal (lower right)
        for i, j in zip(range(row, self.size), range(col, self.size)):
            if self.board[i][j]:
                return False
                
        return True

    def set_first_queen(self):
        """Get user input for the first queen's position and place it on the board."""
        while True:
            try:
                print("\nEnter coordinates of first queen:")
                row = int(input(f"Enter row (1-{self.size}): "))
                col = int(input(f"Enter column (1-{self.size}): "))
                
                if not (1 <= row <= self.size and 1 <= col <= self.size):
                    raise ValueError("Coordinates must be within board dimensions")
                
                # Convert to 0-based indexing
                row -= 1
                col -= 1
                
                self.board[row][col] = True
                print("\nInitial board with first queen:")
                self.print_board()
                return
                
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Please try again.")

    def solve(self, row: int) -> bool:
        """
        Solve the N-Queens problem using backtracking.
        
        Args:
            row (int): Current row being processed
            
        Returns:
            bool: True if a solution is found, False otherwise
        """
        if row == self.size:
            self.count += 1
            # Store the current solution
            solution = [row[:] for row in self.board]
            self.solutions.append(solution)
            return True
        
        # Skip row if it already has a queen
        if any(self.board[row]):
            return self.solve(row + 1)

        found_solution = False
        for col in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = True
                found_solution = self.solve(row + 1) or found_solution
                self.board[row][col] = False
                
        return found_solution

    def display_solutions(self):
        """Display all found solutions and final message."""
        if self.count > 0:
            print(f"\nFound {self.count} solution{'s' if self.count > 1 else ''}!")
            for i, solution in enumerate(self.solutions, 1):
                print(f"\nSolution {i}:")
                print("  " + " ".join([str(i + 1) for i in range(self.size)]))
                for row_num, row in enumerate(solution, 1):
                    print(f"{row_num} ", end="")
                    for cell in row:
                        print("Q" if cell else ".", end=" ")
                    print()
        else:
            print("\nNo solutions exist for the given first queen position.")

def main():
    """Main function to run the N-Queens solver."""
    try:
        solver = NQueens()
        solver.set_first_queen()
        solver.solve(0)
        solver.display_solutions()
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()