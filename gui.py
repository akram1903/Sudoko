
from tkinter import *
import copy
import time
import Sudoku_Backtracking
import backtrackingForGui
import generatePuzzle
NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'

SCALE = 0.7
if __name__=='__main__':
    window = Tk()
    window.geometry(f"{int(SCALE*1300)}x{int(SCALE*910)}")
    window.title("Suduko agent")
    window.config(background="#404258")
    window.resizable(False,False)

    radioButtonsVar = IntVar(window, 1) 
    canvas = Canvas(window,height=900*SCALE,width=900*SCALE,background="#50577A")
    button = None

    current_state:list[list[int]] =  []
    for i in range(9):
        current_state.append([])
        for j in range(9):
            current_state[i].append(0)

    modeSelected=0
    selectedPlace=[-1,-1]

    
    # for making the gui faster
    environment:list=[]
    rectangleIds=[]
    numberIds=[]
    selectionLines=[]
    selectionBlock=None
    for i in range(9):
        # rectangleIds.append([])
        numberIds.append([])
        for j in range(9):
            # rectangleIds[i].append([])
            numberIds[i].append(0)

def printKeys(event):
    print(event.keysym+" key pressed")
    if event.keysym in ["1","2","3","4","5","6","7","8","9","BackSpace","space"]:
        editSelectedTile(event)

def terminate(event):
    exit()

# ============ not done ==============
def genPuzzle():
    global current_state
    certificate,current_state=generatePuzzle.generatePuzzle()
    drawPuzzle()
    unselect()

def solvePuzzle():
    global current_state
    # print(current_state)
    copyOfState = copy.deepcopy(current_state)
    if Sudoku_Backtracking.Backtracking_Solver(copyOfState,0,0):
        print("Soduko board Solved !!")
        Sudoku_Backtracking.print_board(copyOfState)  
        # drawPuzzle()
        # window.update()
        
        solve_sudoku(current_state)
        drawPuzzle()
        canvas.update()
    else:
        print("No Solution For This Sudoku")

    # if Sudoku_Backtracking.Backtracking_Solver(current_state,0,0):
    #     print("Soduko board Solved !!")
    #     Sudoku_Backtracking.print_board(current_state)  
    #     drawPuzzle()
    # else:
    #     print("No Solution For This Sudoku")


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
        if backtrackingForGui.is_valid_move(grid,row,col,num):
            grid[row][col] = num 
            editTileOn(row,col,num)
            time.sleep(0.25)
            if (Backtracking_Solver(grid,row,col+1)): 
                return True
            
        grid[row][col]=0
        editTileOn(row,col,num)

        
    return False

            
# ====================================

def mode1():
    global modeSelected,button
    unselect()
    modeSelected = 1
    print(modeSelected)
    if button is None:
        button = Button(window,text='generate puzzle',font=('arial',17),foreground='#D6E4E5',background="#404258",command=genPuzzle)
        button.place(x=950*SCALE,y=425*SCALE)
    
    else:
        button.config(text='generate puzzle',command=genPuzzle)

def mode2():
    global modeSelected,button
    unselect()
    modeSelected = 2
    print(modeSelected)
    if button is None:
        button = Button(window,text='Solve',font=('arial',17),foreground='#D6E4E5',background="#404258",command=solvePuzzle)
        button.place(x=950*SCALE,y=425*SCALE)
    else:
        button.config(text='Solve',command=solvePuzzle)


def mode3():

    # global modeSelected,button
    # unselect()
    # modeSelected = 3
    # print(modeSelected)
    # if button is None:
    #     button = Button(window,text='Solve',font=('arial',17),foreground='#D6E4E5',background="#404258",command=solvePuzzle)
    #     button.place(x=950*SCALE,y=425*SCALE)
    # else:
    #     button.config(text='user solve',command=interactive)
    pass

def drawRadioButtons():
    global window,radioButtonsVar
    
    Radiobutton(window, text = "generate puzzle", variable = radioButtonsVar, 
        value = 1, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode1).place(x=SCALE*950,y=SCALE*100,) 
    Radiobutton(window, text = "ai solve", variable = radioButtonsVar, 
        value = 2, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode2).place(x=SCALE*950,y=SCALE*150)
    Radiobutton(window, text = "Interactive", variable = radioButtonsVar, 
        value = 3, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode3).place(x=SCALE*950,y=SCALE*200)
    

def drawEnvironment():
    global environment
    
    while environment.__len__()>0:
        canvas.delete(environment.pop())

    for i in range(9):
        environment.append(canvas.create_line(100*i*SCALE,0,100*i*SCALE,900*SCALE,width=2*SCALE))
        environment.append(canvas.create_line(0,100*i*SCALE,900*SCALE,100*i*SCALE,width=2*SCALE))

    environment.append(canvas.create_line(300*SCALE,0,300*SCALE,900*SCALE,width=5*SCALE))
    environment.append(canvas.create_line(600*SCALE,0,600*SCALE,900*SCALE,width=5*SCALE))
    environment.append(canvas.create_line(0,300*SCALE,900*SCALE,300*SCALE,width=5*SCALE))
    environment.append(canvas.create_line(0,600*SCALE,900*SCALE,600*SCALE,width=5*SCALE))



def drawPuzzle():
    global current_state,numberIds
    

    
    for i in range(9):
        for j in range(9):
            canvas.delete(numberIds[i][j])
            element = current_state[i][j]
            if element == 0:
                element = ' '
            numberIds[i][j]=canvas.create_text((j*100+50)*SCALE,(i*100+50)*SCALE,text=f'{element}',font=('arial',40),fill='#D6E4E5')


def keyPressed(event):
    print(event.keysym)
    num = event.keysym
    arr = ["1","2","3","4","5","6","7","8","space","BackSpace","0"]

    if num in arr:
        # if event.keysym == "space" or event.keysym == "0":
        #     num = None
        print("available key")

def selectPlace(event):
    global selectedPlace
    unselect()
    if(event.x>900*SCALE or event.y>900*SCALE):
        print('out of canvas')
        return
    
    colSelected = (event.x//(100*SCALE))
    rowSelected = (event.y//(100*SCALE))
    print('x=',event.x,'\ty=',event.y)
    print('index of col',colSelected)
    print('index of row',rowSelected,end='\n\n')
    selectedPlace = [int(rowSelected),int(colSelected)]

    drawSelectedTile()
    
# unselect only on gui selectedPlace haven't been touched
def unselect(event=None):
    global selectedPlace
    if(selectedPlace[0]>-1):
        j,i=selectedPlace[0],selectedPlace[1]
        element = current_state[j][i]
        if element == 0:
            element = ' '
        
        canvas.delete(selectionBlock)
            
        while(selectionLines.__len__()>0):
            canvas.delete(selectionLines.pop())

        

def drawSelectedTile():
    global numberIds,selectionBlock,selectionLines

    j,i=selectedPlace[0],selectedPlace[1]
    if selectionBlock is not None:
        canvas.delete(selectionBlock)
    selectionBlock=canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=SELECTED_TILE_COLOR)
    element= current_state[j][i]
    if element == 0:
        element = ' '

    canvas.delete(numberIds[j][i])
    numberIds[j][i]=canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{element}',font=('arial',40),fill='#D6E4E5')
    # print(current_state)
    drawEnvironment()
    while(selectionLines.__len__()>0):
        canvas.delete(selectionLines.pop())
    
    selectionLines.append(canvas.create_line(100*i*SCALE,0,100*i*SCALE,900*SCALE,width=2*SCALE,fill=SELECTED_TILE_COLOR))
    selectionLines.append(canvas.create_line(0,100*j*SCALE,900*SCALE,100*j*SCALE,width=2*SCALE,fill=SELECTED_TILE_COLOR))
    selectionLines.append(canvas.create_line(100*(i+1)*SCALE,0,100*(1+i)*SCALE,900*SCALE,width=2*SCALE,fill=SELECTED_TILE_COLOR))
    selectionLines.append(canvas.create_line(0,100*(j+1)*SCALE,900*SCALE,100*(1+j)*SCALE,width=2*SCALE,fill=SELECTED_TILE_COLOR))
    

def changePlace(event):
    global selectedPlace
    flag = False
    if selectedPlace[0] == -1:
        return
    if event.keysym == 'Right':
        if selectedPlace[1]<8:
            unselect()
            flag = True
            selectedPlace[1] += 1
    elif event.keysym == 'Left':
        if selectedPlace[1]>0:
            unselect()
            flag = True
            selectedPlace[1] -= 1
    elif event.keysym == 'Up':
        if selectedPlace[0]>0:
            unselect()
            flag = True
            selectedPlace[0] -= 1
    else :
        if selectedPlace[0]<8:
            unselect()
            flag = True
            selectedPlace[0] += 1
    if flag:
        drawSelectedTile()

def editSelectedTile(event):
    global selectedPlace,canvas,current_state
    j = selectedPlace[0]
    i = selectedPlace[1]

    # canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=SELECTED_TILE_COLOR)
    x = event.keysym
    if x in ['BackSpace','space','0']:
        x = 0
    current_state[j][i]=int(x)
    if x ==0:
        x=' '
    canvas.delete(numberIds[j][i])
    numberIds[j][i]=canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{x}',font=('arial',40),fill='#FFFFFF')
    canvas.update()
    
    

    Sudoku_Backtracking.print_board(current_state)

    drawEnvironment()


def editTileOn(row,col,newValue):
    global selectedPlace
    selectedPlace = [row,col]
    drawSelectedTile()

    x = newValue
    if x in ['BackSpace','space','0']:
        x = 0
    current_state[j][i]=int(x)
    if x ==0:
        x=' '
    canvas.delete(numberIds[j][i])
    numberIds[j][i]=canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{x}',font=('arial',40),fill='#FFFFFF')
    # unselect()
    canvas.update()

def get_empty_cells(grid):
    """Find empty cells (cells with 0) in the Sudoku grid."""
    empty_cells = []
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def is_valid(grid, row, col, num):
    """Check if the current number is valid in the row, column, and box."""
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def get_possible_values(grid, row, col):
    """Get possible values for a given empty cell."""
    possible_values = set(str(i) for i in range(1, 10))
    for x in range(9):
        possible_values.discard(str(grid[row][x]))
        possible_values.discard(str(grid[x][col]))

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            possible_values.discard(str(grid[i + start_row][j + start_col]))

    return possible_values

def solve_sudoku(grid):
    empty_cells = get_empty_cells(grid)
    return solve(empty_cells,grid)

def solve(empty_cells:list,grid):
    if not empty_cells:
        return True

    row, col = empty_cells.pop()
    possible_values = get_possible_values(grid, row, col)
    print(f'for row: {row} col:{col} possible values are {possible_values}')

    for num in possible_values:
        if is_valid(grid, row, col, num):
            grid[row][col] = int(num)
            # editTileOn(row,col,num)
            # time.sleep(0.2)
            if solve(empty_cells,grid):
                editTileOn(row,col,'0')
                time.sleep(0.2)
                return True
            # editTileOn(row,col,'0')
            grid[row][col] = 0  # Backtrack if no valid number found
            # time.sleep(0.2)
    empty_cells.append((row, col))  # Add back the cell for backtracking
    return False  # No valid number found for this cell

if __name__ == "__main__":
    
    # current_state = [[0,7,0,0,0,0,6,8,0],
    #                 [0,0,0,0,7,3,0,0,9],
    #                 [3,0,9,0,0,0,0,4,5],
    #                 [4,9,0,0,0,0,0,0,0],
    #                 [0,0,0,0,0,0,9,0,2],
    #                 [0,0,0,0,0,0,0,3,6],
    #                 [9,6,0,0,0,0,3,0,8],
    #                 [7,0,0,6,8,0,0,0,0],
    #                 [0,2,8,0,0,0,6,8,0],]

    drawEnvironment()
    drawRadioButtons()
    drawPuzzle()
    canvas.place(x=0,y=0)

    canvas.bind('<Button-1>',selectPlace)
    window.bind("<Key>",printKeys)
    
    window.bind("<Escape>",unselect)
    window.bind("<Right>",changePlace)
    window.bind("<Up>",changePlace)
    window.bind("<Down>",changePlace)
    window.bind("<Left>",changePlace)
    
    window.mainloop()