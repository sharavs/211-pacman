import tkinter as tk
from tkinter import *
from tkinter import ttk
from collections import defaultdict
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import * 
#import pygame
import csv
import os
import os.path
import random
import re
import time
import threading
from PIL import ImageTk, Image

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
        self.score = 0
        self.control = parent
        parent.title("Pacman HD")
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

        def quit_game():
            print("quit game")
            self.control.quitter()

        def killed():
            self.control.gameover()

        '''
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
                    #print(self.current)
                elif (self.map[next_right[0]][next_right[1]] == 1):
                    self.move(self.ghostplayer, 0, +self.ghost.speed)
                    #print(self.current)
                elif (self.map[next_right[0]][next_right[1]] == 1) and (self.map[next_down[0]][next_down[1]] == 1):
                    self.move(self.ghostplayer, 0, +15)
                    #print(self.current)
                elif self.current==(19, 19):
                    #print('found')
                    self.move(self.ghostplayer, -self.ghost.speed, 0)
                #elif (self.map[next_left[0]][next_left[1]] != 1):
                #    self.move(self.ghostplayer, 0, -self.ghost.speed)
                else:
                    #print('else')
                    if (self.map[next_left[0]][next_left[1]] != 1):
                        self.move(self.ghostplayer, 0, -self.ghost.speed)
                    else:
                        self.move(self.ghostplayer, 0, +self.ghost.speed)

            else:
                #self.move(self.ghostplayer, -self.ghost.speed*17, -self.ghost.speed*6)
                pass
            self.after(100,move1)
            
            
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

            #print(self.ghost_direction)



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


        '''
        def move(event):
            key_pressed = event.keysym
            print(key_pressed)
            coords = self.coords(self.pacmanplayer)
            y = int(coords[0] / 20)
            x = int(coords[1] / 20)
            #print((x, y))

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
                #while (self.map[next_up[0]][next_up[1]] != 1):
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

                    coords = self.coords(self.pacmanplayer)
                    y = int(coords[0] / 20)
                    x = int(coords[1] / 20)
                    next_up = (x - 1, y)

            if event.keysym == 'Down':
                #while (self.map[next_down[0]][next_down[1]] != 1):
                if (self.map[next_down[0]][next_down[1]] != 1):
                    self.move(self.pacmanplayer,0,self.pacman.speed)
                    self.pacman_newx = next_down[1]
                    self.pacman_newy = next_down[0]
                    if (self.map[next_down[0]][next_down[1]] == 2):
                        self.score += 1
                        self.map[next_down[0]][next_down[1]] = 0
                        self.update_map()
                    else:
                        pass
                    coords = self.coords(self.pacmanplayer)
                    y = int(coords[0] / 20)
                    x = int(coords[1] / 20)
                    next_down = (x + 1, y)

            if event.keysym == 'Left':
                #while(self.map[next_left[0]][next_left[1]] != 1):
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
                    coords = self.coords(self.pacmanplayer)
                    y = int(coords[0] / 20)
                    x = int(coords[1] / 20)
                    next_left = (x, y - 1)

            if event.keysym == 'Right':
                #while(self.map[next_right[0]][next_right[1]] != 1):
                if(self.map[next_right[0]][next_right[1]] != 1):
                    self.move(self.pacmanplayer, +self.pacman.speed, 0)
                    time.sleep(0.01)
                    self.pacman_newx = next_right[1]
                    self.pacman_newy = next_right[0]
                    if (self.map[next_right[0]][next_right[1]] == 2):
                        self.score += 1
                        self.map[next_right[0]][next_right[1]] = 0
                        self.update_map()
                    else:
                        pass
                    coords = self.coords(self.pacmanplayer)
                    y = int(coords[0] / 20)
                    x = int(coords[1] / 20)
                    next_right = (x, y + 1)
            self.after(50,self.move)

            print(self.score)
            '''


        mainmenu = Menu(self)
        parent.config(menu=mainmenu)
        file_option = Menu(mainmenu, tearoff=True)
        mainmenu.add_cascade(label="File", menu=file_option)
        file_option.add_cascade(label="Save Game", command=save_game)
        file_option.add_cascade(label="Load Game", command=openfile)
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
                        wall = self.create_rectangle(x1, y1, x2, y2, fill="navy", tags=str(self.map[row][column]))
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


class BaseScreen    (
    tk.Frame    ):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs,width=500,height=500,bg="black")
        
        self.control    = parent

        style_button = Style() 
        style_button.theme_use('alt')
        style_button.configure(
                'TButton'                       ,
                font = ('calibri', 20, 'bold',) , 
                borderwidth = 0                 ,
                background  = 'black'           ,
                foreground  = 'white'           ,
            )
        style_button.map('TButton', 
            foreground = [('active', '!disabled', 'orange')], 
            background = [('active', 'black')])

        style_label1 = Style() 
        style_label1.theme_use('alt')
        style_label1.configure(
                'a.TLabel'                        ,
                font = ('calibri', 50, 'bold',) , 
                borderwidth = 0                 ,
                background  = 'black'           ,
                foreground  = 'orange'          ,
            )

        style_label2 = Style() 
        style_label2.theme_use('alt')
        style_label2.configure(
                'b.TLabel'                        ,
                font = ('calibri', 10, 'bold',) , 
                borderwidth = 0                 ,
                background  = 'black'           ,
                foreground  = 'white'           ,
            )

        self._frame = tk.Frame(self,bg="black")
        self._frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def _add_image(self):
        img = Image.open("pac-man.png")
        img = img.resize((192, 140),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img, master= self._frame)

        self._image = tk.Label(self._frame, image = img, background= "black")
        self._image.image = img
        self._image.grid(row=0,column=1)

class StartScreen   (
    BaseScreen   ):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._add_image()
        self._button_new    = Button(self._frame, text= "NEW GAME"    ,style = 'TButton',
            command = self.control.new_game )
        self._button_new.grid(row=1,column=1,sticky= 'w')
        
        self._button_load   = Button(self._frame, text= "LOAD GAME"   ,style = 'TButton')
        self._button_load.grid(row=2,column=1,sticky= 'w')

        self._button_help   = Button(self._frame, text= "HELP"        ,style = 'TButton',
            command = lambda : self.control.show_screen(self.control.help_screen))
        self._button_help.grid(row=3,column=1,sticky= 'w')

        self._button_quit   = Button(self._frame, text= "QUIT"        ,style = 'TButton',
            command= self.control.quitter)
        self._button_quit.grid(row=4,column=1,sticky= 'w')

class HelpScreen(
    BaseScreen   ):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self._label1 = Label(self._frame, text= "HELP", style = "a.TLabel")
        self._label1.grid(row=1,column=1)
        
        self._label2 = Label(self._frame, text= "- ARROW KEYS ARE USED TO MOVE PAC-MAN IN THE RELATIVE DIRECTION",
            style = "b.TLabel")
        self._label2.grid(row=2,column=1,sticky="w")

        self._label3 = Label(self._frame, text= "- COLLECT ALL THE FOOD (SMALL DOTS) TO WIN THE GAME",
            style = "b.TLabel")
        self._label3.grid(row=3,column=1,sticky="w")

        self._label4 = Label(self._frame, text= "- AVOID RUNNING INTO THE GHOSTS",
            style = "b.TLabel")
        self._label4.grid(row=4,column=1,sticky="w")

        self._button_quit   = Button(self._frame, text= "MAIN MENU"        ,style = 'TButton',
            command = lambda : self.control.show_screen(self.control.start_screen))
        self._button_quit.grid(row=5,column=1)

class OverScreen    (
    BaseScreen   ):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._add_image()

        score   = kwargs.get('score',0)

        self._label1 = Label(self._frame, text= "GAME OVER", style = "a.TLabel")
        self._label1.grid(row=1,column=1)
        
        self._label2 = Label(self._frame, text= f"YOUR SCORE : {score}",
            style = "a.TLabel")
        self._label2.grid(row=2,column=1)

        self._button_quit   = Button(self._frame, text= "MAIN MENU"        ,style = 'TButton',
            command = lambda : self.control.show_screen(self.control.start_screen))
        self._button_quit.grid(row=3,column=1)

class LoadingScreen    (
    BaseScreen   ):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._add_image()

        score   = kwargs.get('score',0)

        self._label1 = Label(self._frame, text= "LOADING...", style = "a.TLabel")
        self._label1.grid(row=1,column=1)