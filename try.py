import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    # Check if the number is not in the current row, column, and the 3x3 grid
    return not (num in board[row] or
                num in [board[i][col] for i in range(9)] or
                num in [board[i][j] for i in range(row - row % 3, row - row % 3 + 3) 
                        for j in range(col - col % 3, col - col % 3 + 3)])

def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack if the solution is not valid
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

class SudokuSolverGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.create_grid()

        solve_button = tk.Button(master, text="Solve", command=self.solve)
        solve_button.grid(row=10, column=0, columnspan=9)

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                entry = tk.Entry(self.master, width=3, font=('Arial', 14), justify='center')
                entry.grid(row=i, column=j)
                entry.insert(0, str(cell_value) if cell_value != 0 else '')

    def solve(self):
        for i in range(9):
            for j in range(9):
                entry = self.master.grid_slaves(row=i, column=j)[0]
                value = entry.get()
                self.board[i][j] = int(value) if value.isdigit() and 1 <= int(value) <= 9 else 0

        if solve_sudoku(self.board):
            self.update_grid()
            messagebox.showinfo("Sudoku Solver", "Puzzle solved!")
        else:
            messagebox.showerror("Sudoku Solver", "No solution exists!")

    def update_grid(self):
        for i in range(9):
            for j in range(9):
                entry = self.master.grid_slaves(row=i, column=j)[0]
                entry.delete(0, tk.END)
                entry.insert(0, str(self.board[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
