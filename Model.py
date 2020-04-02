import csv
import os
import View as v
import csv
import shelve
from datetime import datetime
import pickle
import os.path

class CSVModel:
    ''' CSV Storage'''
    
    fields = {'ID':None,'Password':None,'Text':None}
    
    
    def __init__(self, saved_data):
            self.saved_data = saved_data
            self.load_data = {}
            
