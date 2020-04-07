import os
import shelve
from datetime import datetime
import pickle
import os.path
import time
import sqlite3

con = sqlite3.connect('pacman.db')

class TXTModel:
    ''' CSV Storage'''

    fields = {'ID': None, 'Password': None, 'Text': None}

    def __init__(self, filename):
        self.filename = filename
        self.filecontent = []
        # self.saved_data = saved_data
        self.tstring = time.strftime("%Y%m%d-%H%M%S")
        self.game_list = []

    def save_game(self, score, map):

        print(score,map)
        try:

            cur = con.cursor()
            print('Connected Successfully')
            cur.execute("CREATE TABLE game(score INT, map STR)")
            cur.execute("INSERT INTO game (score , map) VALUES (?,?)",
                        (score, str(map)))
            print(score,map)

        except sqlite3.Error as error:
            print('SQLite Error: ', error)
            cur = con.cursor()
            cur.execute("INSERT INTO game (score , map) VALUES (?,?)",
                        (score, str(map)))

            cur.execute("SELECT * FROM game")
            rows = cur.fetchall()
            #self.game_list = []
            for row in rows:
                self.game_list.append((row[0],row[1]))
            print('Game List:')
            for i in self.game_list:
                print(i)
            print(self.game_list)

        finally:
            #cur.close()
            #con.close()
            print('Database closed...')

    def load_game(self):
        load_list =[]
        try:

            cur = con.cursor()
            print('Connected Successfully')
            cur.execute("CREATE TABLE game(score INT, map STR)")
            #cur.execute("INSERT INTO game (score , map) VALUES (?,?)",

            rows = cur.fetchall()
            for row in rows:
                load_list.append((row[0],row[1]))
            for i in load_list:
                print(i)
            print('still here')



        except sqlite3.Error as error:
            print('SQLite Error: ', error)
            cur = con.cursor()
            #cur.execute("INSERT INTO game (score , map) VALUES (?,?)",
             #           (score, str(map)))

            cur.execute("SELECT * FROM game")
            rows = cur.fetchall()
            for row in rows:
                load_list.append((row[0], row[1]))
            for i in load_list:
                print(i)

        finally:
                # cur.close()
                # con.close()
                print('Database closed...')

    '''
    def save_game(self, score, map):
        newfile = not os.path.exists('game'+self.tstring)  # check if it's a new file
        if newfile:
            f = open(('game'+self.tstring+'.txt'), 'w')
            f.write('[{}]'.format(str(score)) + '\n')
            f.write(str(map) + '\n')
        else:
            f = open((self.filename, 'w'))
            f.write('[{}]'.format(str(score)) + '\n')
            f.write(str(map) + '\n')
            f.close()
        f.close()

    def load_game(self):
        f = open(self.filename, 'r')
        records = []

        x = 0
        for x in range(2):
            item = f.readline()
            self.filecontent.append(item)
            x += 1
        for i in self.filecontent:
            records.append(i[:-1])
        f.close()
        return records
    '''

    def filer(self):
        file = self.filename
        return file
