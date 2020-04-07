import Model as m
import View as v
from tkinter import filedialog, messagebox
import tkinter as tk
from time import sleep

class Application(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameboard      = v.GameBoard(self)
        self.start_screen   = v.StartScreen(self)
        self.over_screen    = v.OverScreen(self)
        self.loading_screen = v.LoadingScreen(self)
        self.help_screen    = v.HelpScreen(self)
        self.current_screen = None

        self.score = self.gameboard.score

        model = m.TXTModel('default1.txt')
        self.currfile = model.filename

        self.show_screen(self.start_screen)

    def new_game    (
        self    ):
        self.gameboard = v.GameBoard(self)
        self.show_screen(self.gameboard)

    def show_screen (
        self    ,
        screen  ):
        if self.current_screen  == screen   :
            return
        if self.current_screen != None  :
            self.current_screen.grid_forget()
        self.current_screen = screen
        self.current_screen.grid(column=1, row=1, sticky='news')
    
    def save(self):
        self.score = self.gameboard.score
        self.map = self.gameboard.map
        model = m.TXTModel(self.currfile)
        model.save_game(self.score, self.map)

    def load(self):
        model = m.TXTModel(self.currfile)
        stuff = model.load_game()
        self.show_screen(self.gameboard)
        return stuff

    def opener(self):
        model = m.TXTModel(self.currfile)
        while self == 'demo.txt':  # If self still default file break askopenfilename
            break
        else:
            self.file_in = filedialog.askopenfilename(initialdir='C:\Documents\Github\211-pacman',
                                                      filetypes=[('File', '*.txt')],
                                                      title='Search a file')  # Search for a file
            self.currfile = self.file_in  # Set currfile as new file name found above
        
        self.show_screen(self.loading_screen)
        messagebox.showinfo('Load File', 'loading selected file...')
        run = self.load()  # load selected file
        print('File loaded successfully')

    def quitter(self):
        quit_pop = messagebox.askquestion('Quit Application', 'Are you sure you want to quit Pac-Man?')
        if quit_pop == 'yes':
            self.destroy()
        else:
            messagebox.showinfo('Return', 'returning user to PacMan...')
        self.gameboard = v.GameBoard(self)
        self.gameboard.grid()

        #self.game = v.gameboard(self)
    def gameover(self):
        self.show_screen(self.over_screen)
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()
