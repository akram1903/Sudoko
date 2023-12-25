#Based on recursion

#grid example
#9 rows , 9 cols
#0 means no number (undefined)
import copy
import Sudoku_Backtracking
import generatePuzzle
# states = []
# grid=[[0,7,0,0,0,0,6,8,0],
#       [0,0,0,0,7,3,0,0,9],
#       [3,0,9,0,0,0,0,4,5],
#       [4,9,0,0,0,0,0,0,0],
#       [0,0,0,0,0,0,9,0,2],
#       [0,0,0,0,0,0,0,3,6],
#       [9,6,0,0,0,0,3,0,8],
#       [7,0,0,6,8,0,0,0,0],
#       [0,2,8,0,0,0,6,8,0],]
#sudoko has one correct result 
#move in a decision chain if false return and find another chain

#we do ont want to try all the combinations validation function to check if certain try is valide

def is_valid_move(grid,row,col,num):
    #   1-  if we have the same number in row , so it is not valid move
    for col_indx in range(len(grid[0])):
        if grid[row][col_indx]==num:
            return False
     #  2-  if we have the same number in col , so it is not valid move
    for row_indx in range(len(grid)):
        if grid[row_indx][col]==num:
            return False
    
    #   3-  get the box it is inside it
    upper_row =row   -   row  % 3 
    left_col =col   -   col  % 3 
    for row_indx in range(3):
        for col_indx in range (3):
            if grid[upper_row   +   row_indx][left_col +col_indx]==num:
                return False
            
    #   valid move no false now
    return True



def Backtracking_Solver(grid,row,col): 
    
    if col == 9 :
        if row==8: 
            return True
        else:
            row =   row + 1
            col = 0
            
    if grid[row][col]>0: 
        return  Backtracking_Solver(grid,row,col+1)
    for num in range (1,10): 
        if is_valid_move(grid,row,col,num):
            grid[row][col] = num 
            # states.append(copy.deepcopy(grid))

            if (Backtracking_Solver(grid,row,col+1)): 
                return True
            
        grid[row][col]=0
        # states.append(copy.deepcopy(grid))
        
    return False

            
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
        
     
        
if __name__ == '__main__':
#     print("Sudoku Board Before Solving")
#     print_board(grid)  
#     print("________________________________")
#     print("")

#     #   print board after solution       
#     if Backtracking_Solver (grid,0,0):
#         print("Soduko board Solved !!")
#         print_board(grid)  
#     #     for i in range (9):
#     #         for j in range (9):
#     #             print(grid[i][j], end=" ")
#     #         print()
#     else:
#         print("No Solution For This Sudoku")
    
    # certificate = [[4, 5, 3, 7, 1, 2, 8, 6, 9],
    #         [9, 1, 6, 5, 3, 8, 2, 7, 4],
    #         [7, 8, 2, 6, 4, 9, 1, 3, 5],
    #         [1, 4, 8, 9, 6, 7, 3, 5, 2],
    #         [2, 9, 5, 4, 8, 3, 7, 1, 6], 
    #         [6, 3, 7, 2, 5, 1, 4, 9, 8],
    #         [5, 7, 1, 8, 9, 4, 6, 2, 3],
    #         [8, 2, 9, 3, 7, 6, 5, 4, 1],
    #         [3, 6, 4, 1, 2, 5, 9, 8, 7]]

    
    # grid = [[0, 5, 3, 0, 1, 2, 8, 0, 9],
    #         [9, 1, 6, 5, 0, 0, 0, 7, 0],
    #         [0, 0, 2, 0, 0, 0, 1, 3, 0],
    #         [1, 4, 0, 9, 0, 7, 0, 0, 2],
    #         [0, 0, 0, 4, 0, 3, 7, 1, 0], 
    #         [6, 3, 7, 2, 5, 0, 0, 0, 0],
    #         [0, 0, 0, 8, 0, 0, 6, 2, 3],
    #         [0, 0, 0, 3, 0, 6, 0, 0, 1],
    #         [0, 6, 4, 1, 2, 0, 0, 8, 7]]
    
    certificate,grid = generatePuzzle.generatePuzzle()
    if Backtracking_Solver (grid,0,0):
        print("Soduko board Solved !!")
        Sudoku_Backtracking.print_board(grid)

        flag = False
        for i in range(9):
            for j in range(9):
                if certificate[i][j]!=grid[i][j]:
                    flag=True

        if not flag:
            print('solved correctly ;)')
        else:
            print('8aaaaalaaaaat')
    else:
        print("No Solution For This Sudoku")
    
