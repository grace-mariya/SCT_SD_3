import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame, width=5, font=("Arial", 14), justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                self.cells[i][j] = entry

    def create_buttons(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.pack(pady=20)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_grid)
        clear_button.pack(pady=10)

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

    def solve_sudoku(self):
        grid = self.get_grid()

        if self.solve(grid):
            self.fill_grid(grid)
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists for this Sudoku.")

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit():
                    row.append(int(value))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def fill_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, i, j, num):
                            grid[i][j] = num
                            if self.solve(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
