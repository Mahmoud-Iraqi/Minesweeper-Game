from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Customizing the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False , False)


# Customizing frames

#Top frame
top_frame = Frame(
    root,
    bg = 'black',
    width = settings.WIDTH,
    height = utils.height_prct(25)
)

top_frame.place(x = 0 , y = 0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font = ("" , 40)
)

game_title.place(x=utils.width_prct(25) , y=0)

#Left frame
left_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)

left_frame.place( x = 0 , y = utils.height_prct(25) )

#center frame
center_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)

center_frame.place(x = utils.width_prct(25) , y = utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_obj.grid(
            row=x,
            column=y
        )

Cell.random_mines()



Cell.create_cell_counter(left_frame)
Cell.cell_counter_obj.place( x = 0 , y = 0)


#Run the window
root.mainloop()