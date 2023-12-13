#Based on recursion

#grid example
#9 rows , 9 cols
#0 means no number (undefined)
grid=[[0,7,0,0,0,0,6,8,0],
      [0,0,0,0,7,3,0,0,9],
      [3,0,9,0,0,0,0,4,5],
      [4,9,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,9,0,2],
      [0,0,0,0,0,0,0,3,6],
      [9,6,0,0,0,0,3,0,8],
      [7,0,0,6,8,0,0,0,0],
      [0,2,8,0,0,0,6,8,0],]
#sudoko has one correct result 
#move in a decision chain if false return and find another chain

#we do ont want to try all the combinations validation function to check if certain try is valide

def is_valid_move(grid,row,col,num):
    #if we have the same number in row , so it is not valid move
    for col_indx in range(9):
        if grid[row][col_indx]==num:
            return False
     #if we have the same number in col , so it is not valid move
    for row_indx in range(9):
        if grid[row_indx][col]==num:
            return False
    
    #get the box it is inside it
    upper_row =row   -   row  % 3 
    left_col =col   -   col  % 3 
    for row_indx in range(3):
        for col_indx in range (3):
            if grid[upper_row   +   row_indx][left_col +col_indx]==num:
                return False
            
    #   valid move no false now
    return True

def Backtracking_Solver(grid,row,col):
    #Reaching final point
    if col == 9 : #last col we have is 8     so this is overboard
        if row==8: #check reaching last row so sudoko is solved 
            return True
        else:#we need to go to next row  because we found a soln until now no false
            row =   row + 1
            col = 0
            
    if grid[row][col]>0:  #if current cell is already solved go to next col
        return  Backtracking_Solver(grid,row,col+1)  #recursive call next col
    for num in range (1,10): #numbers 1->9
        if is_valid_move(grid,row,col,num):
            grid[row][col] = num #we will assume this is the correct soln 
            #Based on trial and error
            if (Backtracking_Solver(grid,row,col+1)): 
                return True
            
        grid[row][col]=0    #if not valid move 
        
    return False

if Backtracking_Solver (grid,0,0):
    for i in range (9):
        for j in range (9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No Solution For This Sudoku")
        
            

            
        
     
            