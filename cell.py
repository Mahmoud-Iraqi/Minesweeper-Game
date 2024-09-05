from tkinter import Button , Label
import settings
import random
import ctypes
import sys


class Cell:

    cell_counter_obj = None
    cell_count = settings.CELL_COUNT
    all_cells = []


    def __init__(self , x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_mine_candidate = False
        self.is_opened = False
        self.cell_btn_obj = None
        self.x = x
        self.y = y
        Cell.all_cells.append(self)



    def create_btn_object(self , location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>' , self.left_click_action)
        btn.bind('<Button-3>' , self.right_click_action)
        self.cell_btn_obj = btn



    @staticmethod
    def create_cell_counter(laocation):
        lbl = Label(
            laocation ,
            width=12,
            height=4,
            bg='black',
            fg = 'white',
            font=("" , 20),
            text = f"cells left: {Cell.cell_count}"
        )
        Cell.cell_counter_obj = lbl



    def left_click_action(self , event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mines == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.PICKED_MINES:
                ctypes.windll.user32.MessageBoxW(0, "Awesome, You've survived!", "Congratulatios!", 0)
                Cell.show_all_mines()

        
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')



    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, "You stepped on a mine", "Booom!", 0)
        #sys.exit() #if you want to terminate the game each time you step on a mine uncomment this function



    def get_cell(self , x , y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell



    @property
    def surrounding_cells(self):
        cells = []

        for top_cell in range(self.y-1 , self.y+2):
            cells.append( self.get_cell(self.x-1 , top_cell) )

        cells.append(self.get_cell(self.x , self.y-1))
        cells.append(self.get_cell(self.x , self.y+1))

        for bootom_cells in range(self.y-1 , self.y+2):
            cells.append(self.get_cell(self.x+1 , bootom_cells))

        cells = [cell for cell in cells if cell is not None]
        return cells



    @property
    def surrounding_mines(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter



    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_obj.configure(text=f"{self.surrounding_mines}")
            if Cell.cell_counter_obj:
                Cell.cell_counter_obj.configure(text=f"cells left: {Cell.cell_count}")

                self.cell_btn_obj.configure(bg='SystemButtonFace')
        self.is_opened = True



    def right_click_action(self , event):
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(bg='blue')
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False



    @staticmethod
    def random_mines():
        random_cells = random.sample( Cell.all_cells , settings.PICKED_MINES )

        for rndm_cell in random_cells:
            rndm_cell.is_mine = True



    @staticmethod
    def show_all_mines():
        for cell in Cell.all_cells:
            if cell.is_mine:
                cell.cell_btn_obj.configure(bg='yellow')



    def __repr__(self):
        return f" cell({self.x} , {self.y}) "


