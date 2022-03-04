import cmd
import readline
import config.c_config as c_config
import database.d_database as d_database
import modules.m_help as m_help
import modules.m_admins as m_admins
import modules.m_importdata as m_importdata
import modules.m_users as m_users
import modules.m_passwords as m_passwords
import modules.m_computers as m_computers
import modules.m_stats as m_stats
import modules.m_search as m_search
import os.path
import csv
import datetime

from colorama import Fore,Style
from prettytable import *

config_actions = [ "create", "delete", "update", "verify" ]
config_update_parameters = [ "all", "password", "uri", "user" ]

db_actions = [ "connect", "disconnect", "status" ]

admin_actions = [ "domain", "domain=enabled", "schema", "schema=enabled", "enterprise", "enterprise=enabled", "accountOperators", "accountOperators=enabled", "administrators", "administrators=enabled", "backupOperators", "backupOperators=enabled", "printOperators", "printOperators=enabled", "replicators", "replicators=enabled", "serverOperators", "serverOperators=enabled", "adminSDHolder", "adminSDHolder=enabled", "passwordneverexpires", "passwordneverexpires=enabled" ]

import_actions = [ "ntlm", "cracked" ]

user_actions = ["localadmin", "localadmin=enabled", "localadminDC", "localadminDC=enabled", "readlaps", "readlaps=enabled", "passwordneverexpires", "passwordneverexpires=enabled"]

password_actions = [ "changeddate", "changeddate=enabled", "comment", "comment=enabled", "userpassword", "userpassword=enabled" ]

computer_actions = [ "laps", "obsolete" ]

stats_actions = [ "password", "password=enabled" ]
stats_password_parameters = [ "user", "admin", "all" ]

search_actions = [ "user", "user=enabled", "password", "password=enabled", "computer", "description" ]
search_password_parameters = [ "is", "like", "empty", "lm", "user_as_pass" ]
search_description_parameters = [ "is", "like", "not_empty" ]
search_parameters = [ "is", "like" ]

class Shell(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        readline.set_completer_delims(' \t\n')
        self.conf = c_config.Config()
        if not self.conf.verify():
            self.conf.create()
        self.driver = d_database.Database()
        self.driver.connect(self.conf.uri, self.conf.user, self.conf.password)
        self.help = m_help.Help()
        self.prompt = Fore.WHITE + "\U0001F99D > "
        self.cmdloop()

    def preloop(self):
        cmd.Cmd.preloop(self)

    def cmdloop(self):
        while True:
            try:
                super(Shell, self).cmdloop()
                break
            except KeyboardInterrupt:
                print("^C")
    
    def __completion_level(self, words, line):
        nb_words = len(words)
        ending_space = True if line[-1] == ' ' else False

        i = nb_words
        while i > 0:
            if (ending_space and nb_words == i) or (not ending_space and nb_words > i):
                return i
            i -= 1
        return 0

    def __complete_from_list(self, text, list):
        if text:
            return [
                action for action in list
                if action.startswith(text)
            ]
        else:
            return list

    def do_config(self, line):
        args = line.split()
        if len(args) < 1:
            print(Fore.RED,'Missing action : create|delete|verify|update',Fore.WHITE)
        else:
            action = args[0]
            if action == 'create':
                self.conf.create()
                self.driver.connect(self.conf.uri, self.conf.user, self.conf.password)
            elif action == 'delete':
                self.conf.delete()
            elif action == 'verify':
                if self.conf.verify():
                    print(Fore.GREEN,'Database configuration OK',Fore.WHITE)
                else:
                    print(Fore.RED,'Invalid database configuration. Need to run "config create" or "config update all"',Fore.WHITE)
            elif action == 'update':
                if len(args) < 2:
                    print(Fore.RED,'Missing parameters : all|uri|user|password',Fore.WHITE)
                else:
                    parameters = args[1]
                    if parameters == 'all':
                        self.conf.update('all')
                    elif parameters == 'uri':
                        self.conf.update('uri')
                    elif parameters == 'user':
                        self.conf.update('user')
                    elif parameters == 'password':
                        self.conf.update('password')
                    else:
                        print(Fore.RED,'Unrecognized parameter. Expected: all|uri|user|password',Fore.WHITE)
                    self.driver.disconnect()
                    self.driver.connect(self.conf.uri, self.conf.user, self.conf.password)
            else:
                print(Fore.RED,'Unrecognized action. Expected: create|delete|verify|update',Fore.WHITE)

    def do_db(self, line):
        args = line.split()
        if len(args) < 1:
            print(Fore.RED,'Missing action : connect|disconnect|status',Fore.WHITE)
        else:
            action = args[0]
            if action == 'connect':
                if self.driver.driver:
                    self.driver.connect(self.conf.uri, self.conf.user, self.conf.password)
                else:
                    print(Fore.BLUE,'Already connected to database',Fore.WHITE)
            elif action == 'disconnect':
                if self.driver.driver:
                    self.driver.disconnect()
                else:
                    print(Fore.BLUE,'Already disconnected from database',Fore.WHITE)
            elif action == 'status':
                if self.driver.status():
                    print(Fore.GREEN,'Connected to database',Fore.WHITE)

    def do_admin(self,line):
        m_admins.Admins().process(self.driver,line)
            
    def do_import(self,line):
        args = line.split()
        if not self.driver.status():
            print(Fore.RED,'Not connected to database. Need to run "db connect"',Fore.WHITE)
            return
        if len(args) < 1:
            print(Fore.RED,'Missing action : ntlm|cracked',Fore.WHITE)
        elif len(args) < 2:
            print(Fore.RED,'Missing file to import.',Fore.WHITE)
        else:
            action = args[0]
            file = args[1]
            import_task = m_importdata.Import()
            if action == 'ntlm':
                if os.path.isfile(file):
                    import_task.importNTLM(file,self.driver)
                else:
                    print(Fore.RED,'Error : file not found.',Fore.WHITE)
            elif action == 'cracked':
                if os.path.isfile(file):
                    import_task.importPassword(file,self.driver)
                else:
                    print(Fore.RED,'Error : file not found.',Fore.WHITE)
            else:
                print(Fore.RED,'Unrecognized action. Expected: ntlm|cracked',Fore.WHITE)

    def do_user(self, line):
        m_users.Users().process(self.driver,line)
            
    def do_password(self, line):
        m_passwords.Passwords().process(self.driver,line)

    def do_computer(self, line):
        m_computers.Computers().process(self.driver,line)
    
    def do_stats(self, line):
        m_stats.Stats().process(self.driver,line)

    def do_search(self, line):
        m_search.Search().process(self.driver,line)

    def complete_config(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level >= 2:
            if words[1] == 'update':
                return self.__complete_from_list(text, config_update_parameters)
        if level == 1:
            if text:
                return [
                    action for action in config_actions
                    if action.startswith(text)
                ]
            else:
                return config_actions

    def complete_db(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in db_actions
                    if action.startswith(text)
                ]
            else:
                return db_actions

    def complete_admin(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in admin_actions
                    if action.startswith(text)
                ]
            else:
                return admin_actions

    def complete_user(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in user_actions
                    if action.startswith(text)
                ]
            else:
                return user_actions

    def complete_password(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in password_actions
                    if action.startswith(text)
                ]
            else:
                return password_actions

    def complete_import(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in import_actions
                    if action.startswith(text)
                ]
            else:
                return import_actions

    def complete_computer(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level == 1:
            if text:
                return [
                    action for action in computer_actions
                    if action.startswith(text)
                ]
            else:
                return computer_actions

    def complete_stats(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level >= 2:
            if words[1] == 'password' or words[1] == 'password=enabled':
                return self.__complete_from_list(text, stats_password_parameters)
        if level == 1:
            if text:
                return [
                    action for action in stats_actions
                    if action.startswith(text)
                ]
            else:
                return stats_actions

    def complete_search(self, text, line, start_index, end_index):
        words = line.split()
        level = self.__completion_level(words, line)
        if level >= 2:
            if words[1] == 'password' or words[1] == 'password=enabled':
                return self.__complete_from_list(text, search_password_parameters)
            elif words[1] == 'description':
                return self.__complete_from_list(text, search_description_parameters)
            else:
                return self.__complete_from_list(text, search_parameters)
        if level == 1:
            if text:
                return [
                    action for action in search_actions
                    if action.startswith(text)
                ]
            else:
                return search_actions

    def help_admin(self,*args):
        self.help.admin()
    
    def help_computer(self,*args):
        self.help.computer()

    def help_config(self,*args):
        self.help.config()

    def help_db(self,*args):
        self.help.db()

    def help_import(self,*args):
        self.help.importFile()

    def help_password(self,*args):
        self.help.password()

    def help_user(self,*args):
        self.help.user()

    def help_stats(self,*args):
        self.help.stats()

    def help_search(self,*args):
        self.help.search()

    def do_exit(self,*args):
        self.driver.disconnect()
        return True

    def do_EOF(self,line):
        """Do exit"""
        self.driver.disconnect()
        return True
