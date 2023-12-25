
import random
import copy
import Sudoku_Backtracking

# if not ( i==3*(i//3)+(k//3) and j==3*(j//3)+k%3) :
#    blockArc1 = (self.variables[i][j], self.variables[3*(i//3)+(k//3)][3*(j//3)+k%3])
#    self.constraints.append(blockArc1)
def generatePuzzle():
    solvedGrid = [[0 for _ in range(9)] for _ in range(9)]
    # grid = [[0 for _ in range(9)] for _ in range(9)]

    # grid[0][0]=9
    # print(grid)
    availableInRow =[[] for _ in range(9)]
    availableInCol =[[] for _ in range(9)]
    availableInBox =[[[] for _ in range(3)] for _ in range(3)]
    for i in range(9):
        availableInRow[i]={1,2,3,4,5,6,7,8,9}
        availableInCol[i]={1,2,3,4,5,6,7,8,9}

    for i in range(3):
        for j in range(3):
            availableInBox[i][j]={1,2,3,4,5,6,7,8,9}

    
    for i in range(9):
        for j in range(9):
            availableNumbers=list(availableInCol[j] & availableInRow[i] & availableInBox[i//3][j//3])
            if len(availableNumbers)>=2:
                choiceIndex=random.randint(0,len(availableNumbers)-1)
            elif len(availableNumbers)==1:
                choiceIndex=0
            else:
                print('no available puzzle')
                print('trying another grid')
                return generatePuzzle()

            choice = availableNumbers[choiceIndex]
            solvedGrid[i][j]= choice
            availableInBox[i//3][j//3].remove(choice)
            availableInCol[j].remove(choice)
            availableInRow[i].remove(choice)

    grid = copy.deepcopy(solvedGrid)

    n_of_empty_tiles=random.randint(30,30)
    # n_of_empty_tiles=30
    while(n_of_empty_tiles>0):
        i=random.randint(0,8)
        j=random.randint(0,8)

        if grid[i][j]!=0:
            grid[i][j]=0
            n_of_empty_tiles -=1

    return solvedGrid,grid


if __name__=='__main__':
    solvedPuzzle,puzzle=generatePuzzle()

    Sudoku_Backtracking.print_board(puzzle)
    print('\n\n')
    Sudoku_Backtracking.print_board(solvedPuzzle)
    print()