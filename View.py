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

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (12,27,237)
YELLOW = (250,225,0)

WIDTH = 500
HEIGHT = 500

'''
class Character(pygame.sprite.Sprite):
    #sprite for pacman/ghosts
    def __init__(self,x,y,ppx,ppy,speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ppx = self.x * 20
        self.ppy = self.y * 20
        self.speed = speed
        #self.color = color
        #self.isPacman = isPacman

        self.image = pygame.Surface((20,20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(x=self.ppx,y=self.ppy)

    def update_left(self):
        self.rect.x -= self.speed

    def update_right(self):
        self.rect.x += self.speed

    def update_up(self):
        self.rect.y -= self.speed

    def update_down(self):
        self.rect.y += self.speed


class gameboard():
    def __init__(self, parent, *args, **kwargs):

        #initializing pygame
        pygame.display.init()
        clock = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        self.pacman = Character(1,1,20,20,5)
        print(self.pacman.ppx)
        all_sprites.add(self.pacman)

        # sets up window size
        WINDOW_SIZE = [500,500]
        screen = pygame.display.set_mode(WINDOW_SIZE)



        self.cellwidth = 18
        self.cellheight = 18
        MARGIN = 2
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                    [1, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
                    [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
                    [1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 2, 2, 1, 1, 1, 2, 1, 0, 0, 0, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1],
                    [1, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1],
                    [1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1],
                    [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        #mainloop runs until user quits
        running = True
        while running:

            #did the user click the close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #update characters
            all_sprites.update()

            #draw/render
            screen.fill((0,0,0))

            # displays the level map
            for row in range(20):
                for column in range(21):
                    if self.map[row][column] == 0:
                        pygame.draw.rect(screen, BLACK, [(MARGIN + self.cellwidth) * column + MARGIN,
                                                         (MARGIN + self.cellheight) * row + MARGIN, self.cellwidth,
                                                         self.cellheight])
                    elif self.map[row][column] == 1:
                        # print("ONE")
                        pygame.draw.rect(screen, BLUE, [(MARGIN + self.cellwidth) * column + MARGIN,
                                                        (MARGIN + self.cellheight) * row + MARGIN, self.cellwidth,
                                                        self.cellheight])
                    else:
                        # print("TWO")
                        pygame.draw.rect(screen, WHITE,
                                         [(MARGIN + self.cellwidth) * column + 8, (MARGIN + self.cellheight) * row + 8,
                                          3, 3])


            all_sprites.draw(screen)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pacman.update_left()
                #print(self.map[self.pacman.ppx][self.pacman.ppy])
            if keys[pygame.K_RIGHT]:
                self.pacman.update_right()
                #print(self.map[self.pacman.ppx][self.pacman.ppy])
            if keys[pygame.K_UP]:
                self.pacman.update_up()
                #print(self.map[self.pacman.ppx][self.pacman.ppy])
            if keys[pygame.K_DOWN]:
                self.pacman.update_down()
                #print(self.map[self.pacman.ppx][self.pacman.ppy])


            #if self.pacman and self.map[self.pacman.x][self.pacman.y] == 2:
             #   print("food")

            pygame.display.update()





            pygame.display.flip()

    pygame.quit()
'''


class Player():
    def __init__(self,parent,x,y,speed):
        self.x = x
        self.y = y
        self.ppx = x*20
        self.ppy = y*20
        self.speed = speed

class Ghosts():
    def __init__(self,parent,x,y,speed):
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
        self.direction_list = ['Up', 'Down', 'Right', 'Left']

        self.filecontent = []

        def save_game():
            print("save game")
            self.control.save()

        def load_game(*args):
            print("load game")

            self.data = self.control.load()  # data retrieves its values from self.control (controller parent)
            wordlist = self.data

            self.score = int(wordlist[0][1:-1])
            self.map = []
            final_list =[]
            new_list = []
            i = wordlist[1][1:-1]
            for var in i:
                for col in var:
                    if col == ' ' or col == '[' or col == ']' or col == ',':
                        #print('char')
                        pass
                    elif col == '1' or '2' or '0':
                        #print(col)
                        new_list.append(int(col))
                    else:
                        pass
            print(type(new_list), new_list)
            # Append to final_list
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

            print('final:',final_list) # remove after
            self.map = list(final_list)

            print('____________________________') # remove
            self.update_map()
            # Add pacman and ghost, tell ghost to choose direction
            self.pacman = Player(self, 1, 1, 20)
            self.pacmanplayer = self.create_oval(self.pacman.x * self.cellwidth, self.pacman.y * self.cellwidth,
                                                 (self.pacman.x * self.cellwidth) + self.cellwidth,
                                                 (self.pacman.y * self.cellwidth) + self.cellheight, fill="yellow",
                                                 tags="pacman")

            self.ghost = Ghosts(self, 10, 6, 20)
            self.ghost1 = self.create_oval(self.ghost.x * self.cellwidth, self.ghost.y * self.cellwidth,
                                           (self.ghost.x * self.cellwidth) + self.cellwidth,
                                           (self.ghost.y * self.cellwidth) + self.cellheight, fill="magenta",
                                           tags="ghost")
            # Start Ghosts @nilabh
            ghost_choose_direction()


        def openfile():
            print('opening file...')
            self.control.opener()
            load_game()

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
            print(event.keysym)
            self.direction = event.keysym
            if self.direction == "Right":
                moveright()
            elif self.direction == "Left":
                moveleft()
            elif self.direction == "Up":
                moveup()
            else:
                movedown()

        def keyreleased(event):
            print(event.keysym, "released")

        def ghostmovedown():
            coords = self.coords(self.ghost1)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            next_down = (x + 1, y)

            if (self.map[next_down[0]][next_down[1]] != 1):
                self.move(self.ghost1, 0, +self.ghost.speed)
                self.ghost_newx = next_down[1]
                self.ghost_newy = next_down[0]
                self.after(100, ghostmovedown)
                self.update()
                #self.update_idletasks()
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
                self.after(100, ghostmoveup)
                self.update()
                #self.update_idletasks()
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
                self.after(100, ghostmoveright)
                self.update()
                #self.update_idletasks()
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
                self.after(100, ghostmoveleft)
                self.update()
                #self.update_idletasks()
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


        def move_ghost1():
            coords = self.coords(self.ghost1)
            print(coords)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)

            next_up = (x - 1, y)
            
            self.direction_list = ['Up','Down','Right','Left']
            self.ghost_direction = 'Up'
            if self.ghost_direction == "Up":
                if (self.map[next_up[0]][next_up[1]] != 1):
                    self.move(self.ghost1, 0, -self.ghost.speed)
                    self.ghost_newx = next_up[1]
                    self.ghost_newy = next_up[0]

                else:
                    pass
                #self.after(100, move_ghost)
            else:
                pass
            self.update_map()


            print(self.ghost_direction)


        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)

        file_option.add_cascade(label="Save Game", command=save_game)
        file_option.add_cascade(label="Load Game", command=openfile)
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

        self.pacman = Player(self,1,1,20)
        self.pacmanplayer = self.create_oval(self.pacman.x*self.cellwidth, self.pacman.y*self.cellwidth, (self.pacman.x*self.cellwidth) + self.cellwidth, (self.pacman.y*self.cellwidth) + self.cellheight, fill="yellow", tags="pacman")



        self.ghost = Ghosts(self, 10, 10, 20)
        self.ghost1 = self.create_oval(self.ghost.x * self.cellwidth, self.ghost.y * self.cellwidth,
                                                  (self.ghost.x * self.cellwidth) + self.cellwidth,
                                                  (self.ghost.y * self.cellwidth) + self.cellheight, fill="magenta",
                                                  tags="ghost")

        ghost_choose_direction()
        self.bind_all("<KeyPress>", keypressed)


        self.score_text = self.create_text(50,420,fill="white",text="SCORE: "+str(self.score))

    def update_map(self):
        try:

            self.delete("all")
            self.score_text = self.create_text(50, 420, fill="white", text="SCORE: "+str(self.score))

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


            #move_ghost()
            #self.bind('<Right>', move_right)
            self.bind_all("<KeyPress>",keypressed)

            #move1()  # remove later


        except Exception as e:
            pass


    def clicked(self,tag):
        print(tag)

    def save_game(self):
        print("save game")

    def clicked(self,tag):
        print("clicked")

