import tkinter as tk
from tkinter import *
from tkinter import ttk
from collections import defaultdict
from tkinter import messagebox
from tkinter import filedialog
#import pygame
import csv
import os
import os.path
import random
import re
import time
import threading


class Player():
    def __init__(self,parent,x,y,speed):
        self.x = x
        self.y = y
        self.ppx = x*20
        self.ppy = y*20
        self.speed = speed

class Ghosts(tk.Canvas):
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.ppx = x * 20
        self.ppy = x * 20
        self.speed = speed


class GameBoard(tk.Canvas):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,width=500,height=500,bg="black")
        self.current = (0,0)

        self.control = parent
        self.direction = None
        self.previous = None
        self.previous2 = None
        self.pacman_newx = 1
        self.pacman_newy = 1
        self.direction_list = ['Up', 'Down', 'Right', 'Left']
        self.lives = 3

        def load_game():
            print("load game")


        def quit_game():
            print("quit game")


        def killed():
            self.control.gameover()


        def moveright():
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_right = (x, y + 1)
            if (self.map[next_right[0]][next_right[1]] != 1) and (self.direction == "Right"):
                self.move(self.pacmanplayer, +self.pacman.speed, 0)
                self.pacman_newx = next_right[1]
                self.pacman_newy = next_right[0]
                if (self.map[next_right[0]][next_right[1]] == 2):
                    self.score += 1
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
                    if (self.map[next_left[0]][next_left[1]] == 2):
                        self.score += 1
                        self.map[next_left[0]][next_left[1]] = 0
                        self.update_map()
                    else:
                        pass
                self.after(100,moveleft)
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
                if (self.map[next_down[0]][next_down[1]] == 2):
                    self.score += 1
                    self.map[next_down[0]][next_down[1]] = 0
                    self.update_map()
                else:
                    pass
                self.after(100,movedown)
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
                if (self.map[next_up[0]][next_up[1]] == 2):
                    self.score += 1
                    self.map[next_up[0]][next_up[1]] = 0
                    self.update_map()
                else:
                    pass
                self.after(100,moveup)
            else:
                pass




        def keypressed(event):

            self.direction = event.keysym
            if self.direction == "Right":
                moveright()
            elif self.direction == "Left":
                moveleft()
            elif self.direction == "Up":
                moveup()
            else:
                movedown()

        def check_lives():
            if self.lives == 0:
                self.control.quit()
            else:
                pass

        def ghostmovedown():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)

            if (self.map[next_down[0]][next_down[1]] != 1):
                self.move(self.ghost1, 0, +self.ghost.speed)
                self.ghost_newx = next_down[1]
                self.ghost_newy = next_down[0]
                if (self.pacman_newx*self.cellwidth == self.ghost_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost_newy*self.cellheight):
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
                self.move(self.ghost1, 0,-self.ghost.speed)
                self.ghost_newx = next_up[1]
                self.ghost_newy = next_up[0]
                if (self.pacman_newx*self.cellwidth == self.ghost_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost_newy*self.cellheight):
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
                self.move(self.ghost1, +self.ghost.speed, 0)
                self.ghost_newx = next_right[1]
                self.ghost_newy = next_right[0]
                if (self.pacman_newx * self.cellwidth == self.ghost_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost_newy*self.cellheight):
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
                self.move(self.ghost1, -self.ghost.speed, 0)
                self.ghost_newx = next_left[1]
                self.ghost_newy = next_left[0]
                if (self.pacman_newx*self.cellwidth == self.ghost_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost_newy*self.cellheight):
                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveleft)
                self.update()
            else:
                self.previous = self.ghost_direction
                ghost_choose_direction()



        def ghost_choose_direction():

            self.ghost_direction = random.choice(self.direction_list)
            if self.ghost_direction == self.previous:
                self.after(100,ghost_choose_direction)
            else:
                if self.ghost_direction == "Up":
                    ghostmoveup()
                elif self.ghost_direction == "Down":
                    ghostmovedown()
                elif self.ghost_direction == "Right":
                    ghostmoveright()
                else:
                    ghostmoveleft()

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
                self.move(self.ghost2, 0, +self.ghost.speed)
                self.ghost2_newx = next_down[1]
                self.ghost2_newy = next_down[0]
                if (self.pacman_newx*self.cellwidth == self.ghost2_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost2_newy*self.cellheight):
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
                self.move(self.ghost2, 0,-self.ghost.speed)
                self.ghost2_newx = next_up[1]
                self.ghost2_newy = next_up[0]
                if (self.pacman_newx*self.cellwidth == self.ghost2_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost2_newy*self.cellheight):
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
                self.move(self.ghost2, +self.ghost.speed, 0)
                self.ghost2_newx = next_right[1]
                self.ghost2_newy = next_right[0]
                if (self.pacman_newx*self.cellwidth == self.ghost2_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost2_newy*self.cellheight):
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
                self.move(self.ghost2, -self.ghost.speed, 0)
                self.ghost2_newx = next_left[1]
                self.ghost2_newy = next_left[0]
                if (self.pacman_newx*self.cellwidth == self.ghost2_newx*self.cellwidth and self.pacman_newy*self.cellheight == self.ghost2_newy*self.cellheight):
                    self.lives -= 1
                    check_lives()
                    init()
                self.after(100, ghostmoveleft2)
                self.update()
            else:
                self.previous2 = self.ghost_direction2
                ghost_choose_direction2()



        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)
        file_option.add_cascade(label="Save Game")
        file_option.add_cascade(label="Load Game", command=load_game)
        file_option.add_cascade(label="Quit Game", command=quit_game)

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1],
                    [1,2,1,1,1,1,2,2,2,2,2,2,2,2,2,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
                    [1,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
                    [1,2,2,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,1],
                    [1,2,2,1,1,2,2,2,2,2,0,2,2,2,2,2,1,1,2,2,1],
                    [1,2,2,2,1,1,1,2,1,0,0,0,1,2,1,1,1,2,2,2,1],
                    [1,1,1,2,1,2,2,2,1,0,0,0,1,2,2,2,1,2,1,1,1],
                    [1,2,2,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,1],
                    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
                    [1,2,1,1,1,2,2,2,2,1,1,1,2,2,2,2,1,1,1,2,1],
                    [1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,1,2,1,2,1,2,1,2,2,2,2,2,2,1],
                    [1,2,1,1,1,1,2,2,2,1,2,1,2,2,2,1,1,1,1,2,1],
                    [1,2,1,1,1,1,2,1,1,1,2,1,1,1,2,1,1,1,1,2,1],
                    [1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,2,2,2,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

        self.cellwidth = 20
        self.cellheight = 20
        self.score = 0



        def init():
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
                        open_space = self.create_rectangle(x1, y1, x2, y2, fill="black",tags=str(self.map[row][column]))
                        self.tag_bind(open_space, '<Button-1>', lambda event, tag=self.itemcget(open_space, "tags"):
                        self.clicked(tag))
                    else:
                        food = self.create_rectangle(x1 + 8, y1 + 8, x2 - 8, y2 - 8, fill="white",tags=str(self.map[row][column]))
                        self.tag_bind(food, '<Button-1>', lambda event, tag=self.itemcget(food, "tags"):
                        self.clicked(tag))

            self.pacman = Player(self,1,1,20)
            self.pacmanplayer = self.create_oval(self.pacman.x*self.cellwidth, self.pacman.y*self.cellwidth, (self.pacman.x*self.cellwidth) + self.cellwidth, (self.pacman.y*self.cellwidth) + self.cellheight, fill="yellow", tags="pacman")



            self.ghost = Ghosts(10, 10, 20)
            self.ghost1 = self.create_oval(self.ghost.x * self.cellwidth, self.ghost.y * self.cellwidth,
                                                  (self.ghost.x * self.cellwidth) + self.cellwidth,
                                                  (self.ghost.y * self.cellwidth) + self.cellheight, fill="magenta",
                                                  tags="ghost")

            self.ghost_two = Ghosts(9, 9, 20)
            self.ghost2 = self.create_oval(self.ghost_two.x * self.cellwidth, self.ghost_two.y * self.cellwidth,
                                       (self.ghost_two.x * self.cellwidth) + self.cellwidth,
                                       (self.ghost_two.y * self.cellwidth) + self.cellheight, fill="orange",
                                       tags="ghost")


        init()
        ghost_choose_direction()
        ghost_choose_direction2()
        self.bind_all("<KeyPress>", keypressed)


        self.score_text = self.create_text(50,420,fill="white",text="SCORE: "+str(self.score))
        self.lives_text = self.create_text(380,420,fill="white",text="LIVES: "+str(self.lives))

    def update_map(self):
        try:

            self.delete("all")
            self.score_text = self.create_text(50, 420, fill="white", text="SCORE: "+str(self.score))
            self.lives_text = self.create_text(380, 420, fill="white", text="LIVES: " + str(self.lives))


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


            #move_ghost()
            #self.bind('<Right>', move_right)
            self.bind_all("<KeyPress>",keypressed)

            #move1()  # remove later


        except Exception as e:
            pass

    def save_game(self):
        print("save game")

    def clicked(self,tag):
        print("clicked")

