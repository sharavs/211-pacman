import Model as m
import View as v
from tkinter import filedialog, messagebox
import tkinter as tk


class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameboard = v.GameBoard(self)
        self.gameboard.grid()

        #self.game = v.gameboard(self)
    def gameover(self):
        messagebox.showinfo('Game Over', 'The ghosts got you, wasted...')

    def quit(self):
        self.gameboard.quit()
        
            
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()