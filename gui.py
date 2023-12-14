# import arcade

# arcade.open_window(1080, 720,"8-puzzle AI")
# arcade.set_background_color(arcade.color.DAVY_GREY)

# arcade.start_render()

# arcade.finish_render()

# arcade.run()
from tkinter import *

NORMAL_TILE_COLOR = '#50577A'
SELECTED_TILE_COLOR = '#AAAAAA'

SCALE = 0.7

window = Tk()
window.geometry(f"{int(SCALE*1300)}x{int(SCALE*910)}")
window.title("Suduko agent")
window.config(background="#404258")
window.resizable(False,False)

radioButtonsVar = IntVar(window, 1) 
canvas = Canvas(window,height=900*SCALE,width=900*SCALE,background="#50577A")
button = None

current_state:list =  []
for i in range(9):
    current_state.append([])
    for j in range(9):
        current_state[i].append(' ')

modeSelected=0
selectedPlace=[-1,-1]

def printKeys(event):
    print(event.keysym+" key pressed")
    if event.keysym in ["1","2","3","4","5","6","7","8","9","BackSpace","space"]:
        editSelectedTile(event)

def terminate(event):
    exit()

# ============ not done ==============
def generatePuzzle():
    pass
def solvePuzzle():
    pass
# ====================================

def mode1():
    global modeSelected,button
    modeSelected = 1
    print(modeSelected)
    if button is None:
        button = Button(window,text='generate puzzle',font=('arial',17),foreground='#D6E4E5',background="#404258",command=generatePuzzle)
        button.place(x=950*SCALE,y=425*SCALE)
    
    else:
        button.config(text='generate puzzle')

def mode2():
    global modeSelected,button
    modeSelected = 2
    print(modeSelected)
    if button is None:
        button = Button(window,text='Solve',font=('arial',17),foreground='#D6E4E5',background="#404258",command=solvePuzzle)
        button.place(x=950*SCALE,y=425*SCALE)
    else:
        button.config(text='Solve')


def mode3():
    global modeSelected,button
    modeSelected = 3
    print(modeSelected)
    if button is None:
        button = Button(window,text='Solve',font=('arial',17),foreground='#D6E4E5',background="#404258",command=solvePuzzle)
        button.place(x=950*SCALE,y=425*SCALE)
    else:
        button.config(text='Solve')

def drawRadioButtons():
    global window,radioButtonsVar
    
    Radiobutton(window, text = "solve generated puzzle", variable = radioButtonsVar, 
        value = 1, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode1).place(x=SCALE*950,y=SCALE*100,) 
    Radiobutton(window, text = "solve given puzzle", variable = radioButtonsVar, 
        value = 2, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode2).place(x=SCALE*950,y=SCALE*150)
    Radiobutton(window, text = "Interactive", variable = radioButtonsVar, 
        value = 3, font=('arial',11),foreground='#D6E4E5',background="#404258",command=mode3).place(x=SCALE*950,y=SCALE*200)
    

def drawEnvironment():
    
    for i in range(9):
        canvas.create_line(100*i*SCALE,0,100*i*SCALE,900*SCALE,width=2*SCALE)
        canvas.create_line(0,100*i*SCALE,900*SCALE,100*i*SCALE,width=2*SCALE)

    canvas.create_line(300*SCALE,0,300*SCALE,900*SCALE,width=5*SCALE)
    canvas.create_line(600*SCALE,0,600*SCALE,900*SCALE,width=5*SCALE)
    canvas.create_line(0,300*SCALE,900*SCALE,300*SCALE,width=5*SCALE)
    canvas.create_line(0,600*SCALE,900*SCALE,600*SCALE,width=5*SCALE)



def drawPuzzle():
    global current_state
    
    
    for i in range(9):
        for j in range(9):
            canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{current_state[i][j]}',font=('arial',40),fill='#D6E4E5')


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
    unselect()
    if(event.x>900*SCALE or event.y>900*SCALE):
        print('out of canvas')
        return
    
    colSelected = (event.x//(100*SCALE))
    rowSelected = (event.y//(100*SCALE))
    print('x=',event.x,'\ty=',event.y)
    print('index of col',colSelected)
    print('index of row',rowSelected,end='\n\n')

    j,i=int(rowSelected),int(colSelected)
    canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=SELECTED_TILE_COLOR)
    canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{current_state[j][i]}',font=('arial',40),fill='#D6E4E5')
    selectedPlace = [int(rowSelected),int(colSelected)]
    print(current_state)
    drawEnvironment()

# unselect only on gui selectedPlace haven't been touched
def unselect():
    global selectedPlace
    if(selectedPlace[0]>-1):
        j,i=selectedPlace[0],selectedPlace[1]
        canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=NORMAL_TILE_COLOR)
        canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{current_state[j][i]}',font=('arial',40),fill='#D6E4E5')

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
        j,i=selectedPlace[0],selectedPlace[1]
        canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=SELECTED_TILE_COLOR)
        canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{current_state[i][j]}',font=('arial',40),fill='#D6E4E5')
    drawEnvironment()

def editSelectedTile(event):
    global selectedPlace,canvas,window,current_state
    j = selectedPlace[0]
    i = selectedPlace[1]

    canvas.create_rectangle(i*100*SCALE,j*100*SCALE,(i*100+100)*SCALE,(j*100+100)*SCALE,fill=SELECTED_TILE_COLOR)
    x = event.keysym
    if x in ['BackSpace','space']:
        x = ' '
    canvas.create_text((i*100+50)*SCALE,(j*100+50)*SCALE,text=f'{x}',font=('arial',40),fill='#FFFFFF')
    window.update()
    if x not in ['BackSpace','space']:
        x = int(x)
    current_state[j][i]=x
    # print('in testbind')

    drawEnvironment()

if __name__ == "__main__":
    
    drawEnvironment()
    drawRadioButtons()
    
    canvas.place(x=0,y=0)

    window.bind('<Button-1>',selectPlace)
    window.bind("<Key>",printKeys)
    
    window.bind("<Escape>",terminate)
    window.bind("<Right>",changePlace)
    window.bind("<Up>",changePlace)
    window.bind("<Down>",changePlace)
    window.bind("<Left>",changePlace)
    
    window.mainloop()