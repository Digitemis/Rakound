import os.path
import queries.q_users as q_users
import csv
import datetime
from . import m_output as q_output

from colorama import Fore,Style
from prettytable import *

class Users():
    def process(self, driver, line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : localadmin|localadminDC|passwordneverexpires|readlaps',Fore.WHITE)
        else:
            action = args[0]
            resultwriter = None
            if action == "localadmin":
                resultSet,session = driver.query(q_users.Users().getLocalAdmins("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_localadmin_all.csv')
                session.close()
            elif action == "localadmin=enabled":
                resultSet,session = driver.query(q_users.Users().getLocalAdmins("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_localadmin_enabled.csv')
                session.close()
            elif action == "localadminDC":
                resultSet,session = driver.query(q_users.Users().getLocalAdminsDC("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_localadminDC_all.csv')
                session.close()
            elif action == "localadminDC=enabled":
                resultSet,session = driver.query(q_users.Users().getLocalAdminsDC("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_localadminDC_enabled.csv')
                session.close()
            elif action == "passwordneverexpires":
                resultSet,session = driver.query(q_users.Users().getPasswordNeverExpires("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_pwdnvrexp_all.csv')
                session.close()
            elif action == "passwordneverexpires=enabled":
                resultSet,session = driver.query(q_users.Users().getPasswordNeverExpires("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_pwdnvrexp_enabled.csv')
                session.close()
            elif action == "readlaps":
                resultSet,session = driver.query(q_users.Users().canReadLapsPassword("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_readlaps_all.csv')
            elif action == "readlaps=enabled":
                resultSet,session = driver.query(q_users.Users().canReadLapsPassword("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')
                                     + 'User_readlaps_enabled.csv')
            else:
                print(Fore.RED,'Unrecognized action. Expected: localadmin|localadminDC|passwordneverexpires|readlaps',Fore.WHITE)
