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

        def save_game():
            print("save game")

        def load_game():
            print("load game")

        def quit_game():
            print("quit game")


        def killed():
            self.control.gameover()

        def move1():
            coords1 = self.coords(self.ghostplayer)
            y = int(coords1[0] / 20)
            x = int(coords1[1] / 20)
            next_right = (x,y+1)
            next_left = (x,y-1)
            next_down = (x+1,y)
            next_up = (x-1, y)
            self.current = (x, y)
            if self.current < (18,18):
                if (self.map[next_right[0]][next_right[1]] != 1) and (self.map[next_left[0]][next_left[1]] != 1):
                    self.move(self.ghostplayer, +self.ghost.speed, 0)
                    print(self.current)
                elif (self.map[next_right[0]][next_right[1]] == 1):
                    self.move(self.ghostplayer, 0, +self.ghost.speed)
                    print(self.current)
                elif (self.map[next_right[0]][next_right[1]] == 1) and (self.map[next_down[0]][next_down[1]] == 1):
                    self.move(self.ghostplayer, 0, +15)
                    print(self.current)
                elif self.current==(19, 19):
                    print('found')
                    self.move(self.ghostplayer, -self.ghost.speed, 0)
                #elif (self.map[next_left[0]][next_left[1]] != 1):
                #    self.move(self.ghostplayer, 0, -self.ghost.speed)
                else:
                    print('else')
                    if (self.map[next_left[0]][next_left[1]] != 1):
                        self.move(self.ghostplayer, 0, -self.ghost.speed)
                    else:
                        self.move(self.ghostplayer, 0, +self.ghost.speed)

            else:
                self.move(self.ghostplayer, -self.ghost.speed*17, -self.ghost.speed*6)
            self.after(100,move1)
            '''
            #self.direction = random.choice(('left','right','up','down','left','right','up','down'))
            current = (x, y)

            if self.direction=='down' and (self.map[next_down[0]][next_down[1]] != 1):
                self.move(self.ghostplayer, 0, +self.ghost.speed)
                print('downward')
            elif self.direction=='right' and (self.map[next_right[0]][next_right[1]] != 1):
                self.move(self.ghostplayer, +self.ghost.speed, 0)
                print('rightward')
            elif self.direction == 'up' and (self.map[next_up[0]][next_up[1]] != 1):
                self.move(self.ghostplayer, 0, +self.ghost.speed)
                print('upward')
            elif self.direction=='left' and (self.map[next_left[0]][next_left[1]] != 1):
                self.move(self.ghostplayer, +self.ghost.speed, 0)
                print('leftward')

            else:
                self.direction = random.choice(('left','right','up','down'))
                print('passing..', self.direction)

            self.after(200, move1)
            #self.update_map()
            '''

        def move(event):
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            print((x, y))

            next_right = (x,y+1)
            next_left = (x,y-1)
            next_down = (x+1,y)
            next_up = (x-1, y)
            current = (x, y)
            if current == self.current:
                print("Game Over")
                killed()







            # Player
            if event.keysym == 'Up':
                if (self.map[next_up[0]][next_up[1]] != 1):
                    self.move(self.pacmanplayer,0,-self.pacman.speed)
                    self.pacman_newx = next_up[1]
                    self.pacman_newy = next_up[0]
                    if (self.map[next_up[0]][next_up[1]] == 2):
                        self.score += 1
                        self.map[next_up[0]][next_up[1]] = 0
                        self.update_map()
                    else:
                        pass
                else:
                    pass

            if event.keysym == 'Down':
                if (self.map[next_down[0]][next_down[1]] != 1):
                    self.move(self.pacmanplayer,0,+self.pacman.speed)
                    self.pacman_newx = next_down[1]
                    self.pacman_newy = next_down[0]
                    if (self.map[next_down[0]][next_down[1]] == 2):
                        self.score += 1
                        self.map[next_down[0]][next_down[1]] = 0
                        self.update_map()
                    else:
                        pass
                else:
                    pass

            if event.keysym == 'Left':
                if(self.map[next_left[0]][next_left[1]] != 1):
                    self.move(self.pacmanplayer, -self.pacman.speed, 0)
                    self.pacman_newx = next_left[1]
                    self.pacman_newy = next_left[0]
                    if (self.map[next_left[0]][next_left[1]] == 2):
                        self.score += 1
                        self.map[next_left[0]][next_left[1]] = 0
                        self.update_map()
                    else:
                        pass
                else:
                    pass
            if event.keysym == 'Right':
                if(self.map[next_right[0]][next_right[1]] != 1):
                    self.move(self.pacmanplayer, self.pacman.speed, 0)
                    self.pacman_newx = next_right[1]
                    self.pacman_newy = next_right[0]
                    if (self.map[next_right[0]][next_right[1]] == 2):
                        self.score += 1
                        self.map[next_right[0]][next_right[1]] = 0
                        self.update_map()
                    else:
                        pass
                else:
                    pass
            print(self.score)



        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)
        file_option.add_cascade(label="Save Game", command=save_game)
        file_option.add_cascade(label="Load Game", command=load_game)
        file_option.add_cascade(label="Quit Game", command=quit_game)

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
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

        #self.bind_all('<Key>',move)

        self.ghost = Ghosts(self, 2, 1, 20)
        self.ghostplayer = self.create_oval(self.ghost.x * self.cellwidth, self.ghost.y * self.cellwidth,
                                                  (self.ghost.x * self.cellwidth) + self.cellwidth,
                                                  (self.ghost.y * self.cellwidth) + self.cellheight, fill="magenta",
                                                  tags="ghost")
        self.bind_all('<Key>', move)
        move1()
        #move1(event='<Key>')

        self.score_text = self.create_text(50,420,fill="white",text="SCORE: "+str(self.score))
    def update_map(self):
        try:
            move1() # remove later
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
            self.ghostplayer = self.create_oval(self.ghost_newx * self.cellwidth,
                                                      self.ghost_newy * self.cellwidth,
                                                      (self.ghost_newx * self.cellwidth) + self.cellwidth,
                                                      (self.ghost_newy * self.cellwidth) + self.cellheight,
                                                      fill="magenta",
                                                      tags="ghost")

            self.bind_all('<Key>', move)


        except Exception as e:
            pass

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

