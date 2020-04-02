import Model as m
import View as v
import tkinter as tk


class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.field = v.Field(self)
        #self.field.grid()
        self.gameboard = v.GameBoard(self)
        self.gameboard.grid()


        
            
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()