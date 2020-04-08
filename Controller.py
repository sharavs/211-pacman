import Model as m
import View as v
from tkinter import filedialog, messagebox
import tkinter as tk
from time import sleep
import subprocess


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gameboard = v.GameBoard(self)
        self.start_screen = v.StartScreen(self)
        self.over_screen = v.OverScreen(self)
        self.loading_screen = v.LoadingScreen(self)
        self.help_screen = v.HelpScreen(self)
        self.current_screen = None

        self.score = self.gameboard.score
        self.map = self.gameboard.map
        model = m.SQLModel('pacman.db')
        self.currfile = model.filename
        self.show_screen(self.start_screen)

    def new_game    (
        self    ):
    # NEW GAME MENU OPTION TRIGGER

    self.gameboard = v.GameBoard(self)
    subprocess.call(["afplay", "audio/game_starting.wav"])
    self.show_screen(self.gameboard)

    def show_screen (
        self    ,
        screen):
        # SCREEN PLACEMENT

        if self.current_screen  == screen   :
            return
        if self.current_screen != None  :
            self.current_screen.grid_forget()
        self.current_screen = screen
        self.current_screen.grid(column=1, row=1, sticky='news')
    
    def save(self):
        # Call Save_game in model with score and map

        self.score = self.gameboard.score
        self.map = self.gameboard.map
        model = m.SQLModel(self.currfile)
        model.save_game(self.score, self.map)

    def load(self):
        # Get score and map from load, game (score, map)

        model = m.SQLModel(self.currfile)
        stuff = model.load_game()
        self.show_screen(self.gameboard)
        return stuff

    def quitter(self):
        # QUIT MENU OPTION TRIGGER

        quit_pop = messagebox.askquestion('Quit Pacman', 'Are you sure you want to quit Pacman?')
        if quit_pop == 'yes':
            self.destroy()
        else:
            pass


    def gameover(self):
    # GAME OVER SCREEN TRIGGER

        self.show_screen(self.over_screen)
                 
if __name__ == "__main__":
    app = Application()
    app.mainloop()
