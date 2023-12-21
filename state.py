from variable import *
from arc import *
class State:
    grid:list(list())
    def __init__(self,grid) -> None:
        self.grid = grid
        self.variables = []

        for i in range(9):
            tmp =[]
            for j in range(9):
                if grid[i][j]==0:
                    tmp.append(Variable())
                else:
                    tmp.append(Variable(domain=[grid[i][j]],value=grid[i][j]))
            self.variables.append(tmp)

    def __str__(self) -> str:
        return f'{grid}\n\n{self.variables}\n'


    def ac3(self,arc:Arc)->bool:
        queue = [(arc.Xi, arc.Xj) for Xi in self.variables for Xj in Xi.neighbors()]

        
        

# by rana , but edited by akram , saif shahed 3al kalam dah
def print_values(s:State):

    for i in range (len(s.variables)):
        if i %3 == 0 and i!=0:
            print("- - - - - - - - - - - - - - - - -") #every time we are on horizontal row multiple of 3
        for j in range (len(s.variables[0])): #check every position in the row
            if j % 3 == 0 and j !=0: #if it is multiple of 3 draw vertical line
                print(" | ",end= " ") 
                #end="" means stay on same line 
                
            if j== 8 :
                print(s.variables[i][j])
            else:
                print(str(s.variables[i][j])+" ",end=" ")

if __name__ == '__main__':

    grid=[[0,7,0,0,0,0,6,8,0],
      [0,0,0,0,7,3,0,0,9],
      [3,0,9,0,0,0,0,4,5],
      [4,9,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,9,0,2],
      [0,0,0,0,0,0,0,3,6],
      [9,6,0,0,0,0,3,0,8],
      [7,0,0,6,8,0,0,0,0],
      [0,2,8,0,0,0,6,8,0],]
    
    s = State(grid)

    print_values(s)
        
    # print('ay 7aga')
    # print('ay 7aga 2')
    # print(s)