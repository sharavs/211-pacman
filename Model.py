import os
import shelve
from datetime import datetime
import pickle
import os.path
import time
import sqlite3

con = sqlite3.connect('pacman.db')

class SQLModel:

    ''' SQL Database Storage'''

    def __init__(self, filename):
        self.filename = filename
        self.filecontent = []
        self.game_list = []

    def save_game(self, score, map):
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
            for row in rows:
                self.game_list.append((row[0],row[1]))
            print('Game List:')
            for i in self.game_list:
                print(i)
            print(self.game_list)
        finally:
            print('Database closed...')

    def load_game(self):
        load_list =[]
        try:
            cur = con.cursor()
            print('Connected Successfully')
            cur.execute("CREATE TABLE game(score INT, map STR)")
            rows = cur.fetchall()
            for row in rows:
                load_list.append((row[0],row[1]))
            for i in load_list:
                print(i)
            print('still here')
        except sqlite3.Error as error:
            print('SQLite Error: ', error)
            cur = con.cursor()
            cur.execute("SELECT * FROM game")
            rows = cur.fetchall()
            for row in rows:
                load_list.append((row[0], row[1]))
            for i in load_list:
                print(i)
            index = int(input('Which game would you like to load? Please write index starting from 0.'))
            score = load_list[index][0]
            map = load_list[index][1]
            print(type(map), map)
            return score, map
        finally:
            print('Database closed...')

    def filer(self):
        file = self.filename
        return file
