import os.path
import csv
import datetime

from colorama import Fore, Style
from prettytable import *

class Output():
    def __init__(self, resultSet):
        self.keys = resultSet.keys()
        self.results = resultSet.data()

    def printTable(self):
        row = []
        count = 0
        table = PrettyTable(hrules=prettytable.ALL)
        table.field_names = self.keys
        table.max_width = 100
        for data in self.results:
            for key in self.keys:
                if type(data[key]) is list:
                    row.append('\n'.join(data[key]))
                else:
                    row.append(data[key])
            table.add_row(row)
            row.clear()
            count += 1
        print(table)
        print("\nFound "+str(count)+" occurrence(s)\n")
    
    def createCSV(self, filename):
        export = None
        export = open('exports/'+filename,'a',newline='')
        resultwriter = csv.writer(export)
        resultwriter.writerow(self.keys)
        row = []
        for data in self.results:
            for key in self.keys:
                if type(data[key]) is list:
                    row.append('\n'.join(data[key]))
                else:
                    row.append(data[key])
            resultwriter.writerow(row)
            row.clear()
        export.close()