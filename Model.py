import csv
import os
import View as v
import csv
import shelve
from datetime import datetime
import pickle
import os.path

class TXTModel:
    ''' CSV Storage'''
    
    fields = {'ID':None,'Password':None,'Text':None}
    
    
    def __init__(self, filename):
            self.filename = filename
            self.filecontent = []
            #self.saved_data = saved_data
            self.load_data = {}

    def save_game(self, score, map):
        newfile = not os.path.exists(self.filename)  # check if it's a new file
        f = open(self.filename, 'w')
        if newfile:
            f.write('[{}]'.format(str(score)) + '\n')
            f.write(str(map) + '\n')
        else:
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

    def filer(self):
        file = self.filename
        return file

