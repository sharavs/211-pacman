import Model as m
import View as v
import tkinter as tk


class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameboard = v.GameBoard(self)
        self.gameboard.grid()

        #self.game = v.gameboard(self)

        
            
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()