# IMPLEMENTATION OF AC3 ALGORITHM

import queue
from state import *


#THE MAIN AC-3 ALGORITHM
def AC3(my_state,num):
    q = queue.Queue()
# get pairs of cconstrains for each variable 
    
    for arc in my_state.constraints: 
        q.put(arc)
        # print("----------arcs-----------------")
        # print(Xi.value)
        # print(Xj.value)
        # print("-----------arcs----------------") 
    # print('variable arcs')
    # for arc in my_state.constraints:
    #     print(arc[0].value ,'--->',arc[1].value)
    #     print(arc[0].domain ,'--->',arc[1].domain)

    # print('variable arcs')

    i = 0
    while not q.empty():
        (Xi, Xj) = q.get()
        # print("----------value-----------------")
        # print(Xi.value)
        # print(Xj.value)
        # print("-----------value----------------")
        i = i + 1 
        # print("----------domain-----------------")
        # print(Xi.domain)
        # print(Xj.domain)
        # print("-----------domain----------------")

        if Revise(my_state, Xi, Xj):
            if len(Xi.domain) == 0:
                return False

            # for Xk in (csp.get_constraints_for_variable(Xi) - Xj):
            #    remove elmfrood logicalyy mlha4 lazma
            # for Xk in (my_state.get_constraints_for_variable(Xi).remove(Xj)):
            # ---------------------sssssssssssssaaaaaaaaaaaiiiiiiiiiiiiifffffffff------------------a
            list_1 = my_state.get_constraints_for_variable(Xi)
            list_1.remove(Xj)
            # print(list_1)
            for Xk in list_1:
                q.put((Xk, Xi))
                    # /////////////////

    #display(csp.values)
    return True 

#WORKING OF THE REVISE ALGORITHM-------------------------------222222222222
def Revise(my_state, Xi, Xj):
    revised = False
    # values = set(Xi.domain)
    values = Xi.domain
    
    for x in values:
        if isconsistent(my_state, x, Xi, Xj):

            Xi.domain.remove(x)
            revised = True

    return revised
    # for x in values:
    #     if not isconsistent(my_state, x, Xi, Xj):
    #         Xi.domain.remove(x)
    #         revised = True

    # return revised

#CHECKS IF THE GIVEN ASSIGNMENT IS CONSISTENT ------------------------------------1111111111
def isconsistent(my_state, x, Xi, Xj):
    for y in Xj.domain:
        if y == x:
            return False
    return True
# def isconsistent(my_state, x, Xi, Xj):
# 	for y in Xj.domain:
# 		if Xj in my_state.get_constraints_for_variable(Xi) and y!=x:
# 			return True

# 	return False

#grid example
#9 rows , 9 cols
#0 means no number (undefined)
grid1=[[0,7,0,0,0,0,6,8,0],
      [0,0,0,0,7,3,0,0,9],
      [3,0,9,0,0,0,0,4,5],
      [4,9,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,9,0,2],
      [0,0,0,0,0,0,0,3,6],
      [9,6,0,0,0,0,3,0,8],
      [7,0,0,6,8,0,0,0,0],
      [0,2,8,0,0,0,6,8,0],]
state1 = State(grid = grid1)
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

def Backtracking_Solver(state1,row,col): #Recursive Function
    #   Base Case Reaching final point
    if col == 9 : # last col we have is 8     so this is overboard
        if row==8: #    check reaching last row so sudoko is solved 
            return True
        else:#  we need to go to next row  because we found a soln until now no false
            row =   row + 1
            col = 0
            
    if state1.variables[row][col].value>0:  #if current cell is already solved go to next col
        return  Backtracking_Solver(state1,row,col+1)  #recursive call next col
    for num in range (1,10): #  numbers 1->9
        # print(num)
        num = Variable(value=num)
        if is_valid_move(state1.grid,row,col,num.value):#    check if valid before adding it to board 
            
            # print("--------------------------------")
            # print(num.value,num.domain)
            # print("--------------------------------")

            state1.variables[row][col] = num #  we will assume this is the correct soln 
            # if(AC3(state1,num)):
                #Based on trial and error
            if (Backtracking_Solver(state1,row,col+1)): 
                if(AC3(state1,num)):
                    return True
                
        zer0 = Variable(value=0)
        state1.grid[row][col]=zer0   #if not valid move 
        
    return False

            
def print_board(grid):
    for i in range (len(grid)):
        if i %3 == 0 and i!=0:
            print("- - - - - - - - - - - - - - - - -") #every time we are on horizontal row multiple of 3
        for j in range (len(grid[0])): #check every position in the row
            if j % 3 == 0 and j !=0: #if it is multiple of 3 draw vertical line
                print(" | ",end= " ") 
                #end="" means stay on same line 
                
            if j== 8 :
                print(grid[i][j])
            else:
                print(str(grid[i][j])+" ",end=" ")
        
     
        

print("Sudoku Board Before Solving")
print_board(state1.grid)  
print("________________________________")
print("")

#   print board after solution       
if Backtracking_Solver (state1,0,0):
    print("Soduko board Solved !!")
    print_board(state1.grid)  
#     for i in range (9):
#         for j in range (9):
#             print(grid[i][j], end=" ")
#         print()
else:
    print("No Solution For This Sudoku")