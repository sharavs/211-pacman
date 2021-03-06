import tkinter as tk
from tkinter import *
from tkinter import ttk
from collections import defaultdict
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *
import csv
import os
import os.path
import random
import re
import time
import threading
from PIL import ImageTk, Image
import subprocess

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (12, 27, 237)
YELLOW = (250, 225, 0)

WIDTH = 500
HEIGHT = 500


class Player():
    def __init__(self, parent, x, y, speed):
        self.x = x
        self.y = y
        self.ppx = x * 20
        self.ppy = y * 20
        self.speed = speed


class Ghosts():
    def __init__(self, parent, x, y, speed):
        self.x = x
        self.y = y
        self.ppx = x * 20
        self.ppy = x * 20
        self.speed = speed


class GameBoard(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, width=500, height=500, bg="black")
        self.current = (0, 0)
        self.control = parent
        parent.title('Pac-Man HD 2020.v3')

        self.direction = None
        self.previous = None
        self.previous2 = None
        self.previous3 = None
        self.pacman_newx = 1
        self.pacman_newy = 1
        self.level = 1
        self.direction_list = ['Up', 'Down', 'Right', 'Left']
        self.lives = 3

        #############################
        ##LEVEL LIST FOR THE LEVELS##
        #############################

        self.level_list = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1],
                            [1, 2, 2, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                            [1, 1, 1, 2, 1, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 1, 2, 1, 1, 1],
                            [1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

                           [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1],
                            [1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1],
                            [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 1, 1, 1, 2, 1, 0, 1, 0, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 1],
                            [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

                           [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
                            [1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1],
                            [1, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1],
                            [1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1],
                            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 1, 2, 2, 1],
                            [1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

                           [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
                            [1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 1, 2, 2, 1, 1, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 1, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 1],
                            [1, 2, 2, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1],
                            [1, 2, 1, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1],
                            [1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

                           [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1],
                            [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],
                            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 1],
                            [1, 2, 1, 1, 1, 2, 1, 2, 1, 0, 0, 0, 1, 2, 1, 2, 1, 1, 1, 2, 1],
                            [1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                            [1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                            [1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1],
                            [1, 2, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1],
                            [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
                            [1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1],
                            [1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 1],
                            [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

        self.filecontent = []

        def save_game():
            print("Save Game")
            self.control.save()

        def load_game():
            l_score, l_map = self.control.load()
            filter1 = l_map
            new_list = []
            final_list = []

            for var in filter1:
                if var == ' ' or var == '[' or var == ']' or var == ',':
                    pass
                else:
                    new_list.append(int(var))

            # SETUP FINAL_LIST IN SELF.MAP FORMAT

            final_list.append(new_list[0:21])
            final_list.append(new_list[21:42])
            final_list.append(new_list[42:63])
            final_list.append(new_list[63:84])
            final_list.append(new_list[84:105])
            final_list.append(new_list[105:126])
            final_list.append(new_list[126:147])
            final_list.append(new_list[147:168])
            final_list.append(new_list[168:189])
            final_list.append(new_list[189:210])

            final_list.append(new_list[210:231])
            final_list.append(new_list[231:252])
            final_list.append(new_list[252:273])
            final_list.append(new_list[273:294])
            final_list.append(new_list[294:315])
            final_list.append(new_list[315:336])
            final_list.append(new_list[336:357])
            final_list.append(new_list[357:378])
            final_list.append(new_list[378:399])
            final_list.append(new_list[399:420])

            # SET SCORE AND MAP WITH INT L_SCORE AND FINAL_LIST
            self.score = l_score
            self.map = final_list

            self.pacman_newx = 1
            self.pacman_newy = 1
            self.update_map()

        def quit_game():
            # EXITS MAINLOOP
            self.control.quitter()
            print("Quit Game")

        def check_lives():
            # CHECK PAC-MAN LIFE
            if self.lives == 0:
                subprocess.call(["afplay", "audio/game_over.wav"])
                print("LOST")
                self.killed()
            else:
                pass

        def check_score():
            # DETERMINES WHEN TO CHANGE LEVEL

            if self.level == 1:
                if self.score != 201:
                    pass
                else:
                    self.map = self.level_list[1]
                    self.level = 2
                    init()
            elif self.level == 2:
                if self.score != 412:
                    pass
                else:
                    self.map = self.level_list[2]
                    self.level = 3
                    init()
            elif self.level == 3:
                if self.score != 624:
                    pass
                else:
                    self.map = self.level_list[3]
                    self.level = 4
                    init()
            elif self.level == 4:
                if self.score != 835:
                    pass
                else:
                    self.map = self.level_list[4]
                    self.level = 5
                    init()
            else:
                if self.score == 1039:
                    subprocess.call(["afplay", "audio/player_wins.wav"])
                    # GAME OVER - FINISHED
                    print("FINISHED")
                    self.killed()
                else:
                    pass

        #########################
        # PLAYER MOVE FUNCTIONS #
        #########################

        def moveright():
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_right = (x, y + 1)

            if (self.map[next_right[0]][next_right[1]] != 1) and (self.direction == "Right"):
                self.move(self.pacmanplayer, +self.pacman.speed, 0)
                self.pacman_newx = next_right[1]
                self.pacman_newy = next_right[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS COLLISION WITH GHOST

                    self.lives -= 1
                    subprocess.call(["afplay", "audio/ghost_eats_pacman.wav"])
                    check_lives()
                    init()

                if (self.map[next_right[0]][next_right[1]] == 2):
                    self.score += 1
                    check_score()
                    self.map[next_right[0]][next_right[1]] = 0
                    self.update_map()
                else:
                    pass
                self.after(100, moveright)

            else:
                pass

        def moveleft():
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_left = (x, y - 1)

            if (self.map[next_left[0]][next_left[1]] != 1) and (self.direction == "Left"):
                if (self.map[next_left[0]][next_left[1]] != 1):
                    self.move(self.pacmanplayer, -self.pacman.speed, 0)
                    self.pacman_newx = next_left[1]
                    self.pacman_newy = next_left[0]

                    if (
                            self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight) or (
                            self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight) or (
                            self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                        # IF STATEMENT CHECKS COLLISION WITH GHOST

                        self.lives -= 1
                        subprocess.call(["afplay", "audio/ghost_eats_pacman.wav"])
                        check_lives()
                        init()

                    if (self.map[next_left[0]][next_left[1]] == 2):
                        self.score += 1
                        check_score()
                        self.map[next_left[0]][next_left[1]] = 0
                        self.update_map()
                    else:
                        pass
                self.after(100, moveleft)
            else:
                pass

        def movedown():
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)

            if (self.map[next_down[0]][next_down[1]] != 1) and (self.direction == "Down"):
                self.move(self.pacmanplayer, 0, self.pacman.speed)
                self.pacman_newx = next_down[1]
                self.pacman_newy = next_down[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS COLLISION WITH GHOST

                    self.lives -= 1
                    subprocess.call(["afplay", "audio/ghost_eats_pacman.wav"])
                    check_lives()
                    init()

                if (self.map[next_down[0]][next_down[1]] == 2):
                    self.score += 1
                    check_score()
                    self.map[next_down[0]][next_down[1]] = 0
                    self.update_map()
                else:
                    pass
                self.after(100, movedown)
            else:
                pass

        def moveup():
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_up = (x - 1, y)

            if (self.map[next_up[0]][next_up[1]] != 1) and (self.direction == "Up"):
                self.move(self.pacmanplayer, 0, -self.pacman.speed)
                self.pacman_newx = next_up[1]
                self.pacman_newy = next_up[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight) or (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS COLLISION WITH GHOST

                    self.lives -= 1
                    subprocess.call(["afplay", "audio/ghost_eats_pacman.wav"])
                    check_lives()
                    init()

                if (self.map[next_up[0]][next_up[1]] == 2):
                    self.score += 1
                    check_score()
                    self.map[next_up[0]][next_up[1]] = 0
                    self.update_map()
                else:
                    pass
                self.after(100, moveup)
            else:
                pass

        def keypressed(event):
            # DETERMINES WHICH KEY IS PRESSED AND EXECUTES FUNCTION ACCORDINGLY

            self.direction = event.keysym
            if self.direction == "Right":
                moveright()
            elif self.direction == "Left":
                moveleft()
            elif self.direction == "Up":
                moveup()
            else:
                movedown()

        ##########################
        # GHOST 1 MOVE FUNCTIONS #
        ##########################

        def ghostmovedown():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)

            if (self.map[next_down[0]][next_down[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost1, 0, +self.ghost.speed)
                self.ghost_newx = next_down[1]
                self.ghost_newy = next_down[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight):
                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmovedown)
                self.update()
            else:
                self.previous = self.ghost_direction
                ghost_choose_direction()

        def ghostmoveup():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_up = (x - 1, y)

            if (self.map[next_up[0]][next_up[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost1, 0, -self.ghost.speed)
                self.ghost_newx = next_up[1]
                self.ghost_newy = next_up[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveup)
                self.update()
            else:
                self.previous = self.ghost_direction
                ghost_choose_direction()

        def ghostmoveright():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_right = (x, y + 1)

            if (self.map[next_right[0]][next_right[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost1, +self.ghost.speed, 0)
                self.ghost_newx = next_right[1]
                self.ghost_newy = next_right[0]
                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveright)
                self.update()
            else:
                self.previous = self.ghost_direction
                ghost_choose_direction()

        def ghostmoveleft():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_left = (x, y - 1)

            if (self.map[next_left[0]][next_left[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost1, -self.ghost.speed, 0)
                self.ghost_newx = next_left[1]
                self.ghost_newy = next_left[0]
                # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN
                if (
                        self.pacman_newx * self.cellwidth == self.ghost_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost_newy * self.cellheight):
                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveleft)
                self.update()
            else:
                self.previous = self.ghost_direction
                ghost_choose_direction()


        def ghost_choose_direction():
            # LOGIC TO GIVE GHOST A RANDOM DIRECTION TO EXECUTE
            # FUNCTION RUNS AGAIN WHEN GHOST IS STUCK

            self.ghost_direction = random.choice(self.direction_list)
            if self.ghost_direction == self.previous:
                self.after(100, ghost_choose_direction)
            else:
                if self.ghost_direction == "Up":
                    ghostmoveup()
                elif self.ghost_direction == "Down":
                    ghostmovedown()
                elif self.ghost_direction == "Right":
                    ghostmoveright()
                else:
                    ghostmoveleft()


        #########################
        # GHOST2 MOVE FUNCTIONS #
        #########################

        def ghost_choose_direction2():

            self.ghost_direction2 = random.choice(self.direction_list)
            if self.ghost_direction2 == self.previous2:
                self.after(100, ghost_choose_direction2)
            else:
                if self.ghost_direction2 == "Up":
                    ghostmoveup2()
                elif self.ghost_direction2 == "Down":
                    ghostmovedown2()
                elif self.ghost_direction2 == "Right":
                    ghostmoveright2()
                else:
                    ghostmoveleft2()

        def ghostmovedown2():
            coords = self.coords(self.ghost2)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)
            if (self.map[next_down[0]][next_down[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost2, 0, +self.ghost.speed)
                self.ghost2_newx = next_down[1]
                self.ghost2_newy = next_down[0]
                if (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmovedown2)
                self.update()
            else:
                self.previous2 = self.ghost_direction2
                ghost_choose_direction2()

        def ghostmoveup2():
            coords = self.coords(self.ghost2)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_up = (x - 1, y)

            if (self.map[next_up[0]][next_up[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost2, 0, -self.ghost.speed)
                self.ghost2_newx = next_up[1]
                self.ghost2_newy = next_up[0]
                if (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveup2)
                self.update()
            else:
                self.previous2 = self.ghost_direction2
                ghost_choose_direction2()

        def ghostmoveright2():
            coords = self.coords(self.ghost2)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_right = (x, y + 1)

            if (self.map[next_right[0]][next_right[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost2, +self.ghost.speed, 0)
                self.ghost2_newx = next_right[1]
                self.ghost2_newy = next_right[0]
                if (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveright2)
                self.update()
            else:
                self.previous2 = self.ghost_direction2
                ghost_choose_direction2()

        def ghostmoveleft2():
            coords = self.coords(self.ghost2)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_left = (x, y - 1)

            if (self.map[next_left[0]][next_left[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost2, -self.ghost.speed, 0)
                self.ghost2_newx = next_left[1]
                self.ghost2_newy = next_left[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost2_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost2_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveleft2)
                self.update()
            else:
                self.previous2 = self.ghost_direction2
                ghost_choose_direction2()


        #########################
        ##GHOST1 MOVE FUNCTIONS##
        #########################

        def ghost_choose_direction3():

            self.ghost_direction3 = random.choice(self.direction_list)
            if self.ghost_direction3 == self.previous3:
                self.after(100, ghost_choose_direction3())
            else:
                if self.ghost_direction3 == "Up":
                    ghostmoveup3()
                elif self.ghost_direction3 == "Down":
                    ghostmovedown3()
                elif self.ghost_direction3 == "Right":
                    ghostmoveright3()
                else:
                    ghostmoveleft3()

        def ghostmovedown3():
            coords = self.coords(self.ghost3)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)
            if (self.map[next_down[0]][next_down[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost3, 0, +self.ghost.speed)
                self.ghost3_newx = next_down[1]
                self.ghost3_newy = next_down[0]
                if (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PAC MAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmovedown3)
                self.update()
            else:
                self.previous3 = self.ghost_direction3
                ghost_choose_direction3()

        def ghostmoveup3():
            coords = self.coords(self.ghost3)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_up = (x - 1, y)

            if (self.map[next_up[0]][next_up[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost3, 0, -self.ghost.speed)
                self.ghost3_newx = next_up[1]
                self.ghost3_newy = next_up[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveup3)
                self.update()
            else:
                self.previous3 = self.ghost_direction3
                ghost_choose_direction3()

        def ghostmoveright3():
            coords = self.coords(self.ghost3)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_right = (x, y + 1)

            if (self.map[next_right[0]][next_right[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost3, +self.ghost.speed, 0)
                self.ghost3_newx = next_right[1]
                self.ghost3_newy = next_right[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveright3)
                self.update()
            else:
                self.previous3 = self.ghost_direction3
                ghost_choose_direction3()

        def ghostmoveleft3():
            coords = self.coords(self.ghost3)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_left = (x, y - 1)

            if (self.map[next_left[0]][next_left[1]] != 1):
                # IF GHOST CAN MOVE

                self.move(self.ghost3, -self.ghost.speed, 0)
                self.ghost3_newx = next_left[1]
                self.ghost3_newy = next_left[0]

                if (
                        self.pacman_newx * self.cellwidth == self.ghost3_newx * self.cellwidth and self.pacman_newy * self.cellheight == self.ghost3_newy * self.cellheight):
                    # IF STATEMENT CHECKS GHOST COLLISION WITH PACMAN

                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveleft3)
                self.update()
            else:
                self.previous3 = self.ghost_direction3
                ghost_choose_direction3()

                
        # MAIN MENU CODE

        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)

        file_option.add_cascade(label="Save Game", command=save_game)
        file_option.add_cascade(label="Load Game", command=load_game)
        file_option.add_cascade(label="Quit Game", command=quit_game)

        # LEVEL STARTS OFF AT MAP 1

        self.map = self.level_list[0]

        self.cellwidth = 20
        self.cellheight = 20
        self.score = 0

        def init():
            # INITIALIZE ALL COMPONENTS

            self.delete("all")
            self.score_text = self.create_text(50, 420, fill="white", text="SCORE: " + str(self.score))
            self.lives_text = self.create_text(380, 420, fill="white", text="LIVES: " + str(self.lives))
            self.level_lext = self.create_text(200, 420, fill="white", text="LEVEL: " + str(self.level))
            for row in range(20):
                for column in range(21):
                    x1 = column * self.cellwidth
                    y1 = row * self.cellheight
                    x2 = x1 + self.cellwidth
                    y2 = y1 + self.cellheight

                    if self.map[row][column] == 1:
                        wall = self.create_rectangle(x1, y1, x2, y2, fill="blue", tags=str(self.map[row][column]))
                        self.tag_bind(wall, '<Button-1>', lambda event, tag=self.itemcget(wall, "tags"):
                        self.clicked(tag))

                    elif self.map[row][column] == 0:
                        open_space = self.create_rectangle(x1, y1, x2, y2, fill="black",
                                                           tags=str(self.map[row][column]))
                        self.tag_bind(open_space, '<Button-1>', lambda event, tag=self.itemcget(open_space, "tags"):
                        self.clicked(tag))
                    else:
                        food = self.create_rectangle(x1 + 8, y1 + 8, x2 - 8, y2 - 8, fill="white",
                                                     tags=str(self.map[row][column]))
                        self.tag_bind(food, '<Button-1>', lambda event, tag=self.itemcget(food, "tags"):
                        self.clicked(tag))

            self.pacman = Player(self, 1, 1, 20)
            self.pacmanplayer = self.create_oval(self.pacman.x * self.cellwidth, self.pacman.y * self.cellwidth,
                                                 (self.pacman.x * self.cellwidth) + self.cellwidth,
                                                 (self.pacman.y * self.cellwidth) + self.cellheight, fill="yellow",
                                                 tags="pacman")

            self.ghost = Ghosts(self, 10, 10, 20)
            self.ghost1 = self.create_oval(self.ghost.x * self.cellwidth, self.ghost.y * self.cellwidth,
                                           (self.ghost.x * self.cellwidth) + self.cellwidth,
                                           (self.ghost.y * self.cellwidth) + self.cellheight, fill="magenta",
                                           tags="ghost")

            self.ghost_two = Ghosts(self, 9, 9, 20)
            self.ghost2 = self.create_oval(self.ghost_two.x * self.cellwidth, self.ghost_two.y * self.cellwidth,
                                           (self.ghost_two.x * self.cellwidth) + self.cellwidth,
                                           (self.ghost_two.y * self.cellwidth) + self.cellheight, fill="orange",
                                           tags="ghost")

            self.ghost_three = Ghosts(self, 9, 9, 20)
            self.ghost3 = self.create_oval(self.ghost_three.x * self.cellwidth, self.ghost_three.y * self.cellwidth,
                                           (self.ghost_three.x * self.cellwidth) + self.cellwidth,
                                           (self.ghost_three.y * self.cellwidth) + self.cellheight, fill="green",
                                           tags="ghost")

        init()
        ghost_choose_direction()
        ghost_choose_direction2()
        ghost_choose_direction3()
        self.bind_all("<KeyPress>", keypressed)

    def update_map(self):
        # MAP UPDATES EVERYTIME PAC MAN MOVES
        # DRAWS PAC MAN & ALL GHOSTS AT THEIR NEW LOCATION
        # PAC MAN: self.pacman_newx, self.pacman_newy
        # GHOST: self.ghost_newx, self.ghost_newy

        try:

            self.delete("all")
            self.score_text = self.create_text(50, 420, fill="white", text="SCORE: " + str(self.score))
            self.lives_text = self.create_text(380, 420, fill="white", text="LIVES: " + str(self.lives))
            self.level_lext = self.create_text(200, 420, fill="white", text="LEVEL: " + str(self.level))

            for row in range(20):
                for column in range(21):
                    x1 = column * self.cellwidth
                    y1 = row * self.cellheight
                    x2 = x1 + self.cellwidth
                    y2 = y1 + self.cellheight

                    if self.map[row][column] == 1:
                        wall = self.create_rectangle(x1, y1, x2, y2, fill="blue", tags=str(self.map[row][column]))
                        self.tag_bind(wall, '<Button-1>', lambda event, tag=self.itemcget(wall, "tags"):
                        self.clicked(tag))

                    elif self.map[row][column] == 0:
                        open_space = self.create_rectangle(x1, y1, x2, y2, fill="black",
                                                           tags=str(self.map[row][column]))
                        self.tag_bind(open_space, '<Button-1>', lambda event, tag=self.itemcget(open_space, "tags"):
                        self.clicked(tag))
                    else:
                        food = self.create_rectangle(x1 + 8, y1 + 8, x2 - 8, y2 - 8, fill="white",
                                                     tags=str(self.map[row][column]))
                        self.tag_bind(food, '<Button-1>', lambda event, tag=self.itemcget(food, "tags"):
                        self.clicked(tag))

            self.pacmanplayer = self.create_oval(self.pacman_newx * self.cellwidth, self.pacman_newy * self.cellwidth,
                                                 (self.pacman_newx * self.cellwidth) + self.cellwidth,
                                                 (self.pacman_newy * self.cellwidth) + self.cellheight, fill="yellow",
                                                 tags="pacman")
            self.ghost1 = self.create_oval(self.ghost_newx * self.cellwidth,
                                           self.ghost_newy * self.cellwidth,
                                           (self.ghost_newx * self.cellwidth) + self.cellwidth,
                                           (self.ghost_newy * self.cellwidth) + self.cellheight,
                                           fill="magenta",
                                           tags="ghost")

            self.ghost2 = self.create_oval(self.ghost2_newx * self.cellwidth,
                                           self.ghost2_newy * self.cellwidth,
                                           (self.ghost2_newx * self.cellwidth) + self.cellwidth,
                                           (self.ghost2_newy * self.cellwidth) + self.cellheight,
                                           fill="orange",
                                           tags="ghost")

            self.ghost3 = self.create_oval(self.ghost3_newx * self.cellwidth,
                                           self.ghost3_newy * self.cellwidth,
                                           (self.ghost3_newx * self.cellwidth) + self.cellwidth,
                                           (self.ghost3_newy * self.cellwidth) + self.cellheight,
                                           fill="green",
                                           tags="ghost")

            self.bind_all("<KeyPress>", keypressed)

        except Exception as e:
            pass

    def clicked(self, tag):
        print(tag)

    def save_game(self):
        print("Save Game")

    def killed(self):
        # INVOKE GAME OVER SCREEN

        self.control.gameover()

    ############################
    #### SCREENS START HERE ####
    ############################

class BaseScreen(
    tk.Frame):
    # BASE SCREEN CLASS

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, width=500, height=500, bg="black")

        self.control = parent

        style_button = Style()
        style_button.theme_use('alt')
        style_button.configure(
            'TButton',
            font=('calibri', 20, 'bold',),
            borderwidth=0,
            background='black',
            foreground='white',
        )
        style_button.map('TButton',
                         foreground=[('active', '!disabled', 'orange')],
                         background=[('active', 'black')])

        style_label1 = Style()
        style_label1.theme_use('alt')
        style_label1.configure(
            'a.TLabel',
            font=('calibri', 50, 'bold',),
            borderwidth=0,
            background='black',
            foreground='orange',
        )

        style_label2 = Style()
        style_label2.theme_use('alt')
        style_label2.configure(
            'b.TLabel',
            font=('calibri', 10, 'bold',),
            borderwidth=0,
            background='black',
            foreground='white',
        )

        self._frame = tk.Frame(self, bg="black")
        self._frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _add_image(self):
        # PAC-MAN GRAPHIC

        img = Image.open("pac-man.png")
        img = img.resize((192, 140), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master=self._frame)

        self._image = tk.Label(self._frame, image=img, background="black")
        self._image.image = img
        self._image.grid(row=0, column=1)


class StartScreen(
    BaseScreen):
    # HOME SCREEN (W/ MAIN MENU)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._add_image()
        self._button_new = Button(self._frame, text="NEW GAME", style='TButton',
                                  command=self.control.new_game)
        self._button_new.grid(row=2, column=1, sticky='w')

 #       self._button_load = Button(self._frame, text="LOAD GAME", style='TButton')
 #       self._button_load.grid(row=2, column=1, sticky='w')

        self._button_help = Button(self._frame, text="HELP", style='TButton',
                                   command=lambda: self.control.show_screen(self.control.help_screen))
        self._button_help.grid(row=3, column=1, sticky='w')

        self._button_quit = Button(self._frame, text="QUIT", style='TButton',
                                   command=self.control.quitter)
        self._button_quit.grid(row=4, column=1, sticky='w')


class HelpScreen(
    BaseScreen):
    # HELP SCREEN (INSTRUCTIONS/ABT)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._label1 = Label(self._frame, text="HELP", style="a.TLabel")
        self._label1.grid(row=1, column=1)

        self._label2 = Label(self._frame, text="- ARROW KEYS ARE USED TO MOVE PAC-MAN IN THE RELATIVE DIRECTION",
                             style="b.TLabel")
        self._label2.grid(row=2, column=1, sticky="w")

        self._label3 = Label(self._frame, text="- COLLECT ALL THE FOOD (SMALL DOTS) TO WIN THE GAME",
                             style="b.TLabel")
        self._label3.grid(row=3, column=1, sticky="w")

        self._label4 = Label(self._frame, text="- AVOID RUNNING INTO THE GHOSTS",
                             style="b.TLabel")
        self._label4.grid(row=4, column=1, sticky="w")

        self._button_quit = Button(self._frame, text="MAIN MENU", style='TButton',
                                   command=lambda: self.control.show_screen(self.control.start_screen))
        self._button_quit.grid(row=5, column=1)


class OverScreen(
    BaseScreen):
    # GAME OVER SCREEN (SCORE, MAIN MENU)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._add_image()

        score = kwargs.get('score', 0)

        self._label1 = Label(self._frame, text="GAME OVER", style="a.TLabel")
        self._label1.grid(row=1, column=1)

        self._label2 = Label(self._frame, text=f"YOUR SCORE : {score}",
                             style="a.TLabel")
        self._label2.grid(row=2, column=1)

        self._button_quit = Button(self._frame, text="MAIN MENU", style='TButton',
                                   command=lambda: self.control.show_screen(self.control.start_screen))
        self._button_quit.grid(row=3, column=1)


class LoadingScreen(
    BaseScreen):
    # LOADING SCREEN - IN CASE OF LOAD/RENDER TIME TO LOAD GAME

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._add_image()

        score = kwargs.get('score', 0)

    def clicked(self, tag):
        print("clicked")

        self._label1 = Label(self._frame, text="LOADING...", style="a.TLabel")
        self._label1.grid(row=1, column=1)
