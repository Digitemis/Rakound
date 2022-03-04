import queries.q_search as q_search
import os.path
import csv
import datetime
from . import m_output as q_output

from colorama import Fore,Style
from prettytable import *

class Search():
    def process(self,driver,line):
        args = line.split()
        if not driver.status():
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : user|computer|password',Fore.WHITE)
        elif len(args) < 2:
            if args[0] == 'user' or args[0] == 'computer' or args[0] == 'user=enabled':
                print(Fore.RED,'Missing filter: is|like',Fore.WHITE)
            elif args[0] == 'password' or args[0] == 'password=enabled':
                print(Fore.RED,'Missing filter: is|like|lm|empty|user_as_pass',Fore.WHITE)
            elif args[0] == 'description':
                print(Fore.RED,'Missing filter: is|like|not_empty',Fore.WHITE)
            else:
                print(Fore.RED,'Invalid action. Expected: user|computer|password|description',Fore.WHITE)
        elif len(args) < 3 and args[1] != 'empty' and args[1] != 'lm' and args[1] != 'user_as_pass' and args[1] != 'not_empty':
            print(Fore.RED,'Missing term : is <term>|like <term>',Fore.WHITE)
        else:
            action = args[0]
            filter = args[1]
            if len(args) > 2:
                term = args[2]
            resultwriter = None
            output = None
            if action == 'user':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchUser("all","is",term.translate(str.maketrans({'\\': r'\\', '"': r'\"'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_user_all.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchUser("all","like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_user_all.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like',Fore.WHITE)
            elif action == 'user=enabled':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchUser("enabled","is",term.translate(str.maketrans({'\\': r'\\', '"': r'\"'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_user_enabled.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchUser("enabled","like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_user_all.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like',Fore.WHITE)
            elif action == 'password':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchPassword("all","is",term.translate(str.maketrans({'\\': r'\\', '\'': r'\\\''}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_all.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchPassword("all","like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_all.csv')
                    session.close()
                elif filter == 'empty':
                    resultSet,session = driver.query(q_search.Search().searchPassword("all","empty",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_all_empty.csv')
                    session.close()
                elif filter == 'lm':
                    resultSet,session = driver.query(q_search.Search().searchPassword("all","lm",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_all_lm.csv')
                    session.close()
                elif filter == 'user_as_pass':
                    resultSet,session = driver.query(q_search.Search().searchPassword("all","user_as_pass",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_all_useraspass.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like|empty|lm|user_as_pass',Fore.WHITE)
            elif action == 'password=enabled':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchPassword("enabled","is",term.translate(str.maketrans({'\\': r'\\', '\'': r'\\\''}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_enabled.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchPassword("enabled","like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_enabled.csv')
                    session.close()
                elif filter == 'empty':
                    resultSet,session = driver.query(q_search.Search().searchPassword("enabled","empty",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_enabled_empty.csv')
                    session.close()
                elif filter == 'lm':
                    resultSet,session = driver.query(q_search.Search().searchPassword("enabled","lm",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_enabled_lm.csv')
                    session.close()
                elif filter == 'user_as_pass':
                    resultSet,session = driver.query(q_search.Search().searchPassword("enabled","user_as_pass",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 2:
                        if "export" in args[2:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_password_enabled_useraspass.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like|empty|lm|user_as_pass',Fore.WHITE)
            elif action == 'computer':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchComputer("is",term.translate(str.maketrans({'\\': r'\\', '"': r'\"'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_computer.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchComputer("like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_computer.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like',Fore.WHITE)
            elif action == 'description':
                if filter == 'is':
                    resultSet,session = driver.query(q_search.Search().searchDescription("is",term.translate(str.maketrans({'\\': r'\\', '"': r'\"'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_description.csv')
                    session.close()
                elif filter == 'like':
                    resultSet,session = driver.query(q_search.Search().searchDescription("like",term.translate(str.maketrans({'\\': r'\\\\', '\'': r'\\\'', '*': r'\\*', '.': r'\\.', '~': '\\\~', '+': r'\\+', '-': r'\\-', '?': r'\\?', '!': r'\\!', '[': r'\\[', ']': r'\\]', '{': r'\\{', '}': r'\\}', '(': r'\\(', ')': r'\\)', '|': r'\\|', '^': r'\\^', '$': r'\\$'}))))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_description.csv')
                    session.close()
                elif filter == 'not_empty':
                    resultSet,session = driver.query(q_search.Search().searchDescription("not_empty",None))
                    output = q_output.Output(resultSet)
                    output.printTable()
                    if len(args) > 3:
                        if "export" in args[3:]:
                            output.createCSV(datetime.datetime.now().strftime('%Y%m%d-%H%M_')+'search_description.csv')
                    session.close()
                else:
                    print(Fore.RED,'Unrecognized filter. Expected: is|like|non_empty',Fore.WHITE)
            else:
                print(Fore.RED,'Unrecognized action. Expected: user|password|computer',Fore.WHITE)
