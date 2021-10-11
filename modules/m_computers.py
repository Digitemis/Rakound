import queries.q_computers as q_computers
import os.path
import csv
import datetime
from . import m_output as q_output

from colorama import Fore,Style
from prettytable import *

class Computers():
    def process(self, driver, line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : laps|obsolete',Fore.WHITE)
        else:
            action = args[0]
            resultwriter = None
            output = None
            if action == "obsolete":
                resultSet,session = driver.query(q_computers.Computers().getObsolete())
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Computer_obsolete.csv')
                session.close()
            elif action == "laps":
                resultSet,session = driver.query(q_computers.Computers().getLAPS())
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'Computer_laps.csv')
                session.close()
            else:
                print(Fore.RED,'Unrecognized action. Expected: laps|obsolete',Fore.WHITE)

