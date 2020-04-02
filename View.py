import tkinter as tk
from tkinter import *
from tkinter import ttk
from collections import defaultdict
from tkinter import messagebox
from tkinter import filedialog
import csv
import os
import os.path
import random
import re


class GameBoard(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,width=500,height=500,bg="black")

        self.control = parent


        def save_game():
            print("save game")

        def load_game():
            print("load game")

        def quit_game():
            print("quit game")



        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)
        file_option.add_cascade(label="Save Game", command=save_game)
        file_option.add_cascade(label="Load Game", command=load_game)
        file_option.add_cascade(label="Quit Game", command=quit_game)

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1],
                    [1,2,1,1,1,1,2,2,2,2,2,2,2,2,2,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,2,1],
                    [1,2,2,1,1,2,2,1,1,2,2,2,1,1,2,2,1,1,2,2,1],
                    [1,2,2,1,1,2,2,1,1,2,2,2,1,1,2,2,1,1,2,2,1],
                    [1,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,1],
                    [1,2,2,2,1,1,1,2,1,0,0,0,1,2,1,1,1,2,2,2,1],
                    [1,2,1,1,1,2,2,2,1,0,0,0,1,2,2,2,1,1,1,2,1],
                    [1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1],
                    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
                    [1,2,1,1,1,2,2,2,2,1,1,1,2,2,2,2,1,1,1,2,1],
                    [1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,1,2,1,2,1,2,1,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,2,2,2,1,2,1,2,2,2,1,1,1,1,2,1],
                    [1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.cellwidth = 20
        self.cellheight = 20

        for row in range(20):
            for column in range(21):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight

                if self.map[row][column] == 1:
                    wall = self.create_rectangle(x1, y1, x2, y2, fill="blue", tags=str(self.map[row][column]))
                    self.tag_bind(wall, '<Button-1>', lambda event, tag=self.itemcget(wall,"tags"):
                            self.clicked(tag))

                elif self.map[row][column]==0:
                    open_space = self.create_rectangle(x1, y1, x2, y2, fill="black", tags=str(self.map[row][column]))
                    self.tag_bind(open_space, '<Button-1>', lambda event, tag=self.itemcget(open_space,"tags"):
                            self.clicked(tag))
                else:
                    food = self.create_rectangle(x1+8, y1+8, x2-8, y2-8, fill="white", tags=str(self.map[row][column]))
                    self.tag_bind(food, '<Button-1>', lambda event, tag=self.itemcget(food,"tags"):
                            self.clicked(tag))

    def clicked(self,tag):
        print(tag)

class ValidEntry(ttk.Entry):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(
            validate='all',
            validatecommand=(self.register(self._validate),
                '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(self.register(self._on_invalid), '%P', '%s', '%S',
                            '%V', '%i', '%d')

            )
        self.error = tk.StringVar()
        self.data = tk.StringVar()
        self.config(textvariable = self.data)

    def Get(self,*args):
        return self.data.get()

    def _toggle_error(self, error=''):

        self.error.set(error)
        if error:
            self.config(foreground='red')
        else:
            self.config(foreground='black')

    def _validate(self, proposed, current, ckey, event, index, action):

        self._toggle_error()
        valid = True

        if event == 'key':
            if action == '0':
                valid = True
            else :
                valid = self._key_validate(proposed, current, ckey, event, index, action)


        elif event == 'focusout':

            valid = self._focusout_validate(event)


        return valid

    def _on_invalid(self, proposed, current, ckey, event, index, action):

        if event != 'key':
            self._toggle_error(self.ErrMsg)

    def _focusout_validate(self, **kwargs):
        return True

    def _key_validate(self, **kwargs):
        return True



class ValidButton(tk.Button):

    def __init__(self, parent, cmd='',*args, **kwargs):
        super().__init__(parent, *args, **kwargs)

