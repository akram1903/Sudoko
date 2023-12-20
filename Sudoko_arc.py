# def ac3(grid):
#     # Initialize queue with all arcs in the Sudoku grid
#     arcs = []
#     for i in range(9):
#         for j in range(9):
#             # Check in the same row
#             for k in range(j + 1, 9):
#                 arcs.append(((i, j), (i, k)))
#             # Check in the same column
#             for k in range(i + 1, 9):
#                 arcs.append(((i, j), (k, j)))
#             # Check in the same 3x3 subgrid
#             for k in range(i // 3 * 3, (i // 3 + 1) * 3):
#                 for l in range(j // 3 * 3, (j // 3 + 1) * 3):
#                     if (k, l) != (i, j):
#                         arcs.append(((i, j), (k, l)))

#     # Initialize domains
#     domains = {(i, j): set(range(1, 10)) for i in range(9) for j in range(9)}

#     # Update domains based on initial puzzle
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] > 0:
#                 domains[(i, j)] = {grid[i][j]}

#     # AC-3 algorithm
#     while arcs:
#         (i, j), (k, l) = arcs.pop(0)
#         if revise(domains, (i, j), (k, l)):
#             if not domains[(i, j)]:
#                 return False  # Inconsistent assignment
#             # Add arcs to check consistency in other affected cells
#             for m in range(9):
#                 if m != k:
#                     arcs.append(((m, k), (i, j)))
#                 if m != l:
#                     arcs.append(((m, l), (i, j)))

#     # Update Sudoku grid based on reduced domains
#     for i in range(9):
#         for j in range(9):
#             if len(domains[(i, j)]) == 1:
#                 grid[i][j] = domains[(i, j)].pop()

#     return True


# def revise(domains, cell1, cell2):
#     revised = False
#     for value in set(domains[cell1]):
#         if all(not is_consistent(value, val2) for val2 in domains[cell2]):
#             domains[cell1].remove(value)
#             revised = True
#     return revised


# def is_consistent(val1, val2):
#     return val1 != val2


# # Example Sudoku grid for testing AC-3 algorithm
# example_grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

# def print_board(grid):
#     for i in range(9):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - -")
#         for j in range(9):
#             if j % 3 == 0 and j != 0:
#                 print("|", end=" ")
#             print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
#         print()

# # Print initial Sudoku board
# print("Sudoku Board Before Solving")
# print_board(example_grid)
# print("_______________________________")

# # Apply AC-3 algorithm
# if ac3(example_grid):
#     print("Sudoku board Solved with AC-3 algorithm!!")
#     print_board(example_grid)
# else:
#     print("No Solution For This Sudoku")
#Based on recursion

#grid example
#9 rows , 9 cols
#0 means no number (undefined)
# grid=[[0,7,0,0,0,0,6,8,0],
#       [0,0,0,0,7,3,0,0,9],
#       [3,0,9,0,0,0,0,4,5],
#       [4,9,0,0,0,0,0,0,0],
#       [0,0,0,0,0,0,9,0,2],
#       [0,0,0,0,0,0,0,3,6],
#       [9,6,0,0,0,0,3,0,8],
#       [7,0,0,6,8,0,0,0,0],
#       [0,2,8,0,0,0,6,8,0],]

# #sudoko has one correct result 
# #move in a decision chain if false return and find another chain

# #we do ont want to try all the combinations validation function to check if certain try is valide
# def is_valid_move(grid, row, col, num):
#     # Check if the move is valid in the row
#     if num in grid[row][col]:
#         return False

#     # Check if the move is valid in the column
#     if num in [grid[i][col][0] for i in range(9)]:
#         return False

#     # Check if the move is valid in the 3x3 box
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if num in grid[start_row + i][start_col + j]:
#                 return False

#     # Valid move
#     return True

# def Backtracking_Solver(grid, row, col):
#     if col == 9:
#         if row == 8:
#             return True
#         else:
#             row += 1
#             col = 0

#     if len(grid[row][col]) == 1:
#         return Backtracking_Solver(grid, row, col + 1)

#     for num in grid[row][col][:]:  # Iterate over a copy of the list
#         if is_valid_move(grid, row, col, num):
#             grid[row][col] = [num]
#             if ac3(grid):
#                 if Backtracking_Solver(grid, row, col + 1):
#                     return True
#             grid[row][col] = grid[row][col][:]  # Restore the original list

#     return False

#     # Valid move
#     return True

# def ac3(grid):
#     queue = []
#     # Initialize queue with all the arcs
#     for i in range(9):
#         for j in range(9):
#             for k in range(j + 1, 9):
#                 queue.append(((i, j), (i, k)))
#                 queue.append(((j, i), (k, i)))
#         #3
    
    

#     while queue:
#         (xi, xj) = queue.pop(0)
#         if revise(grid, xi, xj):
#             if len(grid[xi[0]][xi[1]]) == 0:
#                 return False
#             for xk in set(neighbors(xi)) - {xj}:
#                 queue.append((xk, xi))

# def revise(grid, xi, xj):

#     revised = False
#     for x in grid[xi[0]][xi[1]]:
#         if not any(is_valid_move(grid, xi[0], xi[1], y) for y in grid[xj[0]][xj[1]] if y != x):
#             grid[xi[0]][xi[1]].remove(x)
#             revised = True
#     return revised

# def neighbors(cell):
#     row, col = cell
#     return [(row, j) for j in range(9)] + [(i, col) for i in range(9)]

# def initialize_domain(grid):
#     domains = [[list(range(1, 10)) if grid[i][j] == 0 else [grid[i][j]] for j in range(9)] for i in range(9)]
#     return domains
           
# def print_board(grid):
#     for i in range (len(grid)):
#         if i %3 == 0 and i!=0:
#             print("- - - - - - - - - - - - - - - - -") #every time we are on horizontal row multiple of 3
#         for j in range (len(grid[0])): #check every position in the row
#             if j % 3 == 0 and j !=0: #if it is multiple of 3 draw vertical line
#                 print(" | ",end= " ") 
#                 #end="" means stay on same line 
                
#             if j== 8 :
#                 print(grid[i][j])
#             else:
#                 print(str(grid[i][j])+" ",end=" ")
        


# # Convert grid to use domains
# grid = [[[grid[i][j]] if grid[i][j] != 0 else list(range(1, 10)) for j in range(9)] for i in range(9)]

# # Apply AC-3 algorithm
# ac3(grid)

# print("Sudoku Board Before Solving")
# print_board([[cell[0] if len(cell) == 1 else 0 for cell in row] for row in grid])
# print("________________________________")
# print("")

# # Print board after solution
# if Backtracking_Solver(grid, 0, 0):
#     print("Sudoku board Solved !!")
#     print_board([[cell[0] if len(cell) == 1 else 0 for cell in row] for row in grid])
# else:
#     print("No Solution For This Sudoku")

