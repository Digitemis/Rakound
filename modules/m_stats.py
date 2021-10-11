import queries.q_stats as q_stats
import os.path
import csv
import datetime
from . import m_output as q_output

from colorama import Fore,Style
from prettytable import *

class Stats():
    def process(self,driver,line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : password',Fore.WHITE)
        else:
            action = args[0]
            resultwriter = None
            output = None
            if action == 'password':
                if len(args) < 2:
                    print(Fore.RED,'Missing parameters : user|admin|computer',Fore.WHITE)
                else:
                    parameters = args[1]
                    if parameters == 'user':
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswords("all"))
                        self.computePasswords(resultSet,session,output)
                        table_top10 = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswords10("all"))
                        table_top10.field_names = ["Password (Top 10)","Total"]
                        for record in resultSet:
                                    table_top10.add_row([record["password"],record["total"]])
                        print(table_top10)
                        session.close()
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswordsType("all"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of users",record["users"]])
                        print(table_type)
                        session.close()
                    elif parameters == 'admin':
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswords("all"))
                        self.computePasswords(resultSet,session,output)
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswordsData("all"))
                        output = q_output.Output(resultSet)
                        output.printTable()
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswordsType("all"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of admins",record["users"]])
                            print(table_type)
                        session.close()
                    elif parameters == 'all':
                        resultSet,session = driver.query(q_stats.Stats().analyzeAllPasswords("all"))
                        self.computePasswords(resultSet,session,output)
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeAllPasswordsType("all"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of users",record["users"]])
                            print(table_type)
                        session.close()
                    else:
                        print(Fore.RED,'Unrecognized parameter. Expected : user|admin|computer',Fore.WHITE)
            elif action == 'password=enabled':
                if len(args) < 2:
                    print(Fore.RED,'Missing parameters : user|computer',Fore.WHITE)
                else:
                    parameters = args[1]
                    if parameters == 'user':
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswords("enabled"))
                        self.computePasswords(resultSet,session,output)
                        table_top10 = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswords10("enabled"))
                        table_top10.field_names = ["Password","Total"]
                        for record in resultSet:
                            table_top10.add_row([record["password"],record["total"]])
                        print(table_top10)
                        session.close()
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeUserPasswordsType("enabled"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of users",record["users"]])
                        print(table_type)
                        session.close()
                    elif parameters == 'admin':
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswords("enabled"))
                        self.computePasswords(resultSet,session,output)
                        table_top10 = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswordsData("enabled"))
                        output = q_output.Output(resultSet)
                        output.printTable()
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeAdminPasswordsType("enabled"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of admins",record["users"]])
                        print(table_type)
                        session.close()
                    elif parameters == 'all':
                        resultSet,session = driver.query(q_stats.Stats().analyzeAllPasswords("enabled"))
                        self.computePasswords(resultSet,session,output)
                        table_type = PrettyTable()
                        resultSet,session = driver.query(q_stats.Stats().analyzeAllPasswordsType("enabled"))
                        table_type.field_names = ["Other data","Total"]
                        for record in resultSet:
                            table_type.add_row(["LM hashes",record["lm"]])
                            table_type.add_row(["Cracked passwords",record["cracked"]])
                            table_type.add_row(["Total of users",record["users"]])
                            print(table_type)
                        session.close()
                    else:
                        print(Fore.RED,'Unrecognized parameter. Expected : user|admin|computer',Fore.WHITE)
            else:
                print(Fore.RED,'Unrecognized action. Expected: password',Fore.WHITE)

    def computePasswords(self, resultSet, session, output):
        password_len = { "empty" : 0, "len4" : 0, "len6" : 0, "len8" : 0, "len10" : 0, "len12" : 0, "len14" : 0, "len16" : 0, "lenMore" : 0 }
        password_complexity = { "empty" : 0, "lower" : 0, "upper" : 0, "num" : 0, "spec" : 0, "lower_upper" : 0, "lower_num" : 0, "lower_spec" : 0, "upper_num" : 0, "upper_spec" : 0, "num_spec" : 0, "lower_upper_num" : 0, "lower_upper_spec" : 0, "lower_num_spec" : 0, "upper_num_spec" : 0, "all" : 0 }
        for record in resultSet:
            if not record["password"]:
                password_len["empty"]+=1
            elif len(record["password"]) < 5:
                password_len["len4"]+=1
            elif len(record["password"]) < 7:
                password_len["len6"]+=1
            elif len(record["password"]) < 9:
                password_len["len8"]+=1
            elif len(record["password"]) < 11:
                password_len["len10"]+=1
            elif len(record["password"]) < 13:
                password_len["len12"]+=1
            elif len(record["password"]) < 15:
                password_len["len14"]+=1
            elif len(record["password"]) < 17:
                password_len["len16"]+=1
            else:
                password_len["lenMore"]+=1
            lower, upper, digit, spec = None, None, None, None
            if not record["password"]:
                password_complexity["empty"]+=1
            else:
                for chars in record["password"]:
                    if chars.islower():
                        lower = True
                    elif chars.isupper():
                        upper = True
                    elif chars.isdigit():
                        digit = True
                    else:
                        spec = True
            if lower and upper and spec and digit:
                password_complexity["all"]+=1
            elif upper and digit and spec:
                password_complexity["upper_num_spec"]+=1
            elif lower and digit and spec:
                password_complexity["lower_num_spec"]+=1
            elif lower and upper and spec:
                password_complexity["lower_upper_spec"]+=1
            elif lower and upper and digit:
                password_complexity["lower_upper_num"]+=1
            elif upper and spec:
                password_complexity["upper_spec"]+=1
            elif upper and digit:
                password_complexity["upper_num"]+=1
            elif lower and spec:
                password_complexity["lower_spec"]+=1
            elif lower and digit:
                password_complexity["lower_num"]+=1
            elif lower and upper:
                password_complexity["lower_upper"]+=1
            elif digit and spec:
                password_complexity["num_spec"]+=1
            elif spec:
                password_complexity["spec"]+=1
            elif digit:
                password_complexity["num"]+=1
            elif upper:
                password_complexity["upper"]+=1
            elif lower: 
                password_complexity["lower"]+=1    
        #Print in terminal
        table_length = PrettyTable()
        table_length.field_names = ["Length", "Total"]
        table_length.add_row(["Empty",password_len["empty"]])
        table_length.add_row(["Password <= 4",password_len["len4"]])
        table_length.add_row(["4 < password <= 6",password_len["len6"]])
        table_length.add_row(["6 < password <= 8",password_len["len8"]])
        table_length.add_row(["8 < password <= 10",password_len["len10"]])
        table_length.add_row(["10 < password <= 12",password_len["len12"]])
        table_length.add_row(["12 < password <= 14",password_len["len14"]])
        table_length.add_row(["14 < password <= 16",password_len["len16"]])
        table_length.add_row(["16 < password",password_len["lenMore"]])
        table_length.add_row(["Total",sum(password_len.values())])
                
        table_complexity = PrettyTable()
        table_complexity.field_names = ["Complexity", "Total"]
        table_complexity.add_row(["Empty",password_complexity["empty"]])
        table_complexity.add_row(["Only lowercase (abc)",password_complexity["lower"]])
        table_complexity.add_row(["Only uppercase (ABC)",password_complexity["upper"]])
        table_complexity.add_row(["Only numeric (123)",password_complexity["num"]])
        table_complexity.add_row(["Only special (!*?)",password_complexity["spec"]])
        table_complexity.add_row(["Lowercase and uppercase (abcDEF)",password_complexity["lower_upper"]])
        table_complexity.add_row(["Lowercase and numeric (abc123)",password_complexity["lower_num"]])
        table_complexity.add_row(["Lowercase and special (abc!*?)",password_complexity["lower_spec"]])
        table_complexity.add_row(["Uppercase and numeric (ABC123)",password_complexity["upper_num"]])
        table_complexity.add_row(["Uppercase and special (ABC!*?)",password_complexity["upper_spec"]])
        table_complexity.add_row(["Numeric and special (123!*?)",password_complexity["num_spec"]])
        table_complexity.add_row(["Lowercase, uppercase and numeric (abcDEF123)",password_complexity["lower_upper_num"]])
        table_complexity.add_row(["Lowercase, uppercase and special (abcDEF!*?)",password_complexity["lower_upper_spec"]])
        table_complexity.add_row(["Lowercase, numeric and special (abc123!*?)",password_complexity["lower_num_spec"]])
        table_complexity.add_row(["Uppercase, numeric and special (ABC123!*?)",password_complexity["upper_num_spec"]])
        table_complexity.add_row(["Lowercase, uppercase, numeric and special (abcDEF123!*?)",password_complexity["all"]])
        table_complexity.add_row(["Total",sum(password_complexity.values())])
        if output:
            output.close()
        session.close()
        print(table_length)
        print(table_complexity)
