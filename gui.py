# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *



SCALE = 0.7

window = Tk()
canvas = Canvas(window,height=900*SCALE,width=900*SCALE,background="#50577A")
# labels = [[None]*3]*3
tiles = [[None]*9]*9
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

def terminate(event):
    exit()

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


def drawEnvironment():
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
    for i in range(9):
        for j in range(9):
            canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{i} {j}')
    

# def bfsSelector():
#     global algorithm
#     algorithm = 0
#     print(algorithm)

# def dfsSelector():
#     global algorithm
#     algorithm = 1
#     print(algorithm)

# def a_euclidian():
#     global algorithm
#     algorithm = 2
#     print(algorithm)

# def a_manhattan():
#     global algorithm
#     algorithm = 3
#     print(algorithm)

# def resetPuzzle(event = None):
#     global entrySet,tileIndex,startState,solutionIndex,solutionPath,algorithm

#     entrySet.clear()
#     tileIndex = 0
#     solutionIndex=0
#     solutionPath.clear()
#     algorithm = -1
#     startState=puzzle.PuzzleState([
#         [None,   None    ,None],
#         [None,   None    ,None],
#         [None,   None    ,None]])
    
#     ShowPuzzle(startState)

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
        
        
# =================___edit here___================= 

def keyPressed(event):
    print(event.keysym)
    num = event.keysym
    arr = ["1","2","3","4","5","6","7","8","space","0"]

    if num in arr:
        if event.keysym == "space" or event.keysym == "0":
            num = None
        print("available key")
        buildTile(num)

       
if __name__ == "__main__":

    
    drawEnvironment()

    drawPuzzle()
    

    
    # window.bind("<Left>",goBack)
    # window.bind("<Right>",goForward)
    window.bind("<Escape>",terminate)
    window.bind("<Key>",printKeys)
    # window.bind("<BackSpace>",resetPuzzle)

    # keys to input the puzzle to be solved
    # window.bind("<Key>",keyPressed)
    canvas.place(x=0,y=0)

    window.mainloop()