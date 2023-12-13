# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *



SCALE = 0.7

window = Tk()
radioButtonsVar = IntVar(window, 1) 
canvas = Canvas(window,height=900*SCALE,width=900*SCALE,background="#50577A")
# tilesLabel = [[None]*9]*9
current_state = None     # ????
modeSelected=0
selectedPlace=[-1,-1]

# solutionPath = []
# solutionIndex = 0

# algorithm = -1

# tileIndex = 0

# entrySet = set()

# targetState=puzzle.PuzzleState([
#         [None,   1    ,2],
#         [3,      4    ,5],
#         [6,      7    ,8]])


# hLabel = Label(window,text="00",font=('Arial',11),foreground='#D6E4E5',background="#404258")
# hl = Label(window,text="heuristic=",font=('Arial',11),foreground='#D6E4E5',background="#404258")
# levelLabel = Label(window,text="00",font=('Arial',11),foreground='#D6E4E5',background="#404258")
# ll = Label(window,text="level=",font=('Arial',11),foreground='#D6E4E5',background="#404258")

# hl.place(x=400*SCALE,y=(600+5)*SCALE)
# ll.place(x=400*SCALE,y=(600+45)*SCALE)
# hLabel.place(x=500*SCALE,y=(600+5)*SCALE)
# levelLabel.place(x=500*SCALE,y=(600+45)*SCALE)

# def drag_start(event):
#     widget = event.widget
#     widget.startX=event.x
#     widget.startY=event.y
#     widget.place(x=widget.winfo_x())
    
# def drag_motion(event):
#     widget = event.widget
#     x=widget.winfo_x() - widget.startX + event.x
#     y=widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)




# def goBack(event):
#     global solutionIndex
#     if solutionIndex < solutionPath.__len__()-1:
#         solutionIndex += 1
#         print("back")
#         ShowPuzzle(solutionPath[solutionIndex])
    

# def goForward(event):
#     global solutionIndex
#     if solutionIndex > 0:
#         solutionIndex -= 1
#         ShowPuzzle(solutionPath[solutionIndex])
#         print("forward")

def printKeys(event):
    print(event.keysym+" key pressed")
    if event.keysym in ["1","2","3","4","5","6","7","8","9","BackSpace","space"]:
        testbind(event)

def terminate(event):
    exit()

# ============ not done ==============
def generatePuzzle():
    pass
def solvePuzzle():
    pass
# ====================================


# def ShowPuzzle(outputState):
#     global hLabel
#     global levelLabel
#     for i in range(3):
#             for j in range(3):
#                 if outputState.matrix[i][j] is None or outputState.matrix[i][j] == 0:
#                     labels[i][j] = Label(window,text=f'   ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
#                     labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
#                     continue
#                 labels[i][j] = Label(window,text=f' {outputState.matrix[i][j]} ',font=('Arial',int(120*SCALE)),foreground='#D6E4E5',background="#50577A")
#                 labels[i][j].place(x=5+200*SCALE*j,y=5+200*SCALE*i)
#                 # labels[i][j].bind("<Button-1>",drag_start)
#                 # labels[i][j].bind("<B1-Motion>",drag_motion)
#     if isinstance(outputState,puzzle.PuzzleState):
#         hLabel.config(text=f"{outputState.heuristic}")
#     else:
#         hLabel.config(text="no h for this algorithm")
#     levelLabel.config(text=f"{outputState.level}")

def mode1():
    global modeSelected,solveButton
    modeSelected = 1
    print(modeSelected)
    solveButton = Button(window,text='generate puzzle',font=('arial',17),foreground='#D6E4E5',background="#404258",command=generatePuzzle)
    solveButton.place(x=950*SCALE,y=425*SCALE)
    

def mode2():
    global modeSelected,solveButton
    modeSelected = 2
    print(modeSelected)

    solveButton = Button(window,text='Solve',font=('arial',17),foreground='#D6E4E5',background="#404258",command=solvePuzzle)
    solveButton.place(x=1040*SCALE,y=425*SCALE)

def mode3():
    global modeSelected
    modeSelected = 3
    print(modeSelected)

def drawRadioButtons():
    global window,radioButtonsVar
    
    Radiobutton(window, text = "solve generated puzzle", variable = radioButtonsVar, 
        value = 1, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode1).place(x=SCALE*950,y=SCALE*100,) 
    Radiobutton(window, text = "solve given puzzle", variable = radioButtonsVar, 
        value = 2, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode2).place(x=SCALE*950,y=SCALE*150)
    Radiobutton(window, text = "Interactive", variable = radioButtonsVar, 
        value = 3, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode3).place(x=SCALE*950,y=SCALE*200)
    

def drawEnvironment():
    global tilesLabel

    for i in range(9):
        for j in range(9):
            # tilesLabel[i][j] = Label(window,text=f'{i}',font=('arial',40),foreground='#D6E4E5',background="#50577A")
            # tilesLabel[i][j].place(x=(i*100+20)*SCALE,y=(j*100+3)*SCALE)
            canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{i}',font=('arial',40),fill='#D6E4E5')

    window.geometry(f"{int(SCALE*1300)}x{int(SCALE*910)}")
    window.title("Suduko agent")
    window.config(background="#404258")
    window.resizable(False,False)
    
    for i in range(9):
        canvas.create_line(100*i*SCALE,0,100*i*SCALE,900*SCALE,width=2*SCALE)
        canvas.create_line(0,100*i*SCALE,900*SCALE,100*i*SCALE,width=2*SCALE)

    canvas.create_line(300*SCALE,0,300*SCALE,900*SCALE,width=5*SCALE)
    canvas.create_line(600*SCALE,0,600*SCALE,900*SCALE,width=5*SCALE)
    canvas.create_line(0,300*SCALE,900*SCALE,300*SCALE,width=5*SCALE)
    canvas.create_line(0,600*SCALE,900*SCALE,600*SCALE,width=5*SCALE)



def drawPuzzle():
    global tilesLabel,current_state
    for i in range(9):
        for j in range(9):
            # canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{i} {j}')
            pass

# def buildTile(num):
    
#     global tileIndex,entrySet,startState
#     if tileIndex < 9 :
#         if num not in entrySet:
#             entrySet.add(num)
#             i=tileIndex//3
#             j=tileIndex%3

#             if num is not None:
#                 startState.matrix[i][j] = int(num)
#             else:
#                 startState.matrix[i][j] = None
#             ShowPuzzle(startState)
#             tileIndex += 1
#         else:
#             print("number entered before")
#     if entrySet.__len__()==9:
#         startButton = Button(window,foreground='#D6E4E5',background="#50577A",text='start',command=startSolve,font=('arial',18))
#         startButton.place(x=SCALE*700,y=SCALE*(300))
#         resetButton = Button(window,foreground='#D6E4E5',background="#50577A",text='reset',command=resetPuzzle,font=('arial',14))
#         resetButton.place(x=SCALE*700,y=SCALE*(550))
        
def keyPressed(event):
    print(event.keysym)
    num = event.keysym
    arr = ["1","2","3","4","5","6","7","8","space","BackSpace","0"]

    if num in arr:
        if event.keysym == "space" or event.keysym == "0":
            num = None
        print("available key")

def selectPlace(event):
    global selectedPlace

    if(event.x>900*SCALE or event.y>900*SCALE):
        print('out of canvas')
        return
    
    colSelected = (event.x//(100*SCALE))
    rowSelected = (event.y//(100*SCALE))
    print('x=',event.x,'\ty=',event.y)
    print('index of col',colSelected)
    print('index of row',rowSelected,end='\n\n')
    selectedPlace = [int(colSelected),int(rowSelected)]

def testbind(event):
    global selectedPlace,canvas,window
    i = selectedPlace[0]
    j = selectedPlace[1]

    canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill='#50577A')
    x = event.keysym
    if x in ['BackSpace','space']:
        x = ' '
    canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{x}',font=('arial',40),fill='#D6E4E5')
    window.update()
    print('in testbind')

if __name__ == "__main__":
    
    drawEnvironment()
    drawPuzzle()
    drawRadioButtons()
    
    canvas.place(x=0,y=0)

    window.bind('<Button-1>',selectPlace)
    window.bind("<Key>",printKeys)
    # window.bind("1",testbind)
    
    window.bind("<Escape>",terminate)
    window.mainloop()