import queries.q_passwords as q_passwords
import os.path
import csv
import datetime
from . import m_output as q_output

from colorama import Fore,Style
from prettytable import *

class Passwords():
    def process(self, driver, line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : changeddate|comment|userpassword',Fore.WHITE)
        else:
            action = args[0]
            resultwriter = None
            output = None
            if action == "changeddate":
                try:
                    int(args[1])
                    age = True
                except Exception as e:
                    age = None
                if len(args) > 1 and age:
                    resultSet,session = driver.query(q_passwords.Passwords().getOldPasswords("all",args[1]))
                    check = args[1]
                else:
                    resultSet,session = driver.query(q_passwords.Passwords().getOldPasswords("all"))
                    check = 90
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_changeddate'+str(check)+'_all.csv')
                session.close()
            elif action == "changeddate=enabled":
                try:
                    int(args[1])
                    age = True
                except Exception as e:
                    age = None
                    print("no given"+args[1])
                if len(args) > 1 and age:
                    resultSet,session = driver.query(q_passwords.Passwords().getOldPasswords("enabled",args[1]))
                    check = args[1]
                else:
                    resultSet,session = driver.query(q_passwords.Passwords().getOldPasswords("enabled"))
                    check = 90
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_changeddate'+str(check)+'_enabled.csv')
                session.close()
            elif action == "userpassword":
                resultSet,session = driver.query(q_passwords.Passwords().getUserPassword("all"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_userpassword_all.csv')
                session.close()
            elif action == "userpassword=enabled":
                resultSet,session = driver.query(q_passwords.Passwords().getUserPassword("enabled"))
                output = q_output.Output(resultSet)
                output.printTable()
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_userpassword_enabled.csv')
            elif action == "comment":
                resultSet,session = driver.query(q_passwords.Passwords().getPasswordInComment("all"))
                table = PrettyTable(hrules=prettytable.ALL)
                table.field_names = ["Account", "Status", "Type", "Description"]
                table._max_width = {"Account" : 30, "Description" : 50}
                for record in resultSet:
                    if record["status"] == True:
                        table.add_row([record["account"],"Enabled",record["type"],record["description"]])
                        if resultwriter:
                            resultwriter.writerow([record["account"],"Enabled",record["type"],record["description"]])
                    elif record["status"] == False:
                        table.add_row([record["account"],"Disabled",record["type"],record["description"]])
                        if resultwriter:
                            resultwriter.writerow([record["account"],"Disabled",record["type"],record["description"]])
                    else:
                        table.add_row([record["account"],record["status"],record["type"],record["description"]])
                        if resultwriter:
                            resultwriter.writerow([record["account"],record["status"],record["type"],record["description"]])
                output = q_output.Output(resultSet)
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_comment_all.csv')
                session.close()
                print(table)
            elif action == "comment=enabled":
                resultSet,session = driver.query(q_passwords.Passwords().getPasswordInComment("enabled"))
                table = PrettyTable(hrules=prettytable.ALL)
                table.field_names = ["Account", "Status", "Type", "Description"]
                table._max_width = {"Account" : 30, "Description" : 50}
                for record in resultSet:
                    table.add_row([record["account"],"Enabled",record["type"],record["description"]])
                    if resultwriter:
                        resultwriter.writerow([record["account"],"Enabled",record["type"],record["description"]])
                output = q_output.Output(resultSet)
                if "export" in args:
                    output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'Password_comment_enabled.csv')
                session.close()
                print(table)
            else:
                print(Fore.RED,'Unrecognized action. Expected: changeddate|userpassword|comment',Fore.WHITE)

