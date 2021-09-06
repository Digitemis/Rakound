import configparser
import getpass
from colorama import Fore,  Style


class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        self.conf_file = 'config/config.ini'
        config.read(self.conf_file)
        self.uri = config['Database']['URI']
        self.user = config['Database']['User']
        self.password = config['Database']['Password']

    def print(self):
        print("Database URI : ", self.uri)
        print("Database user : ", self.user)

    def create(self):
        config = configparser.ConfigParser()
        uri = input('Database URI (bolt://) : ')
        while not uri:
            uri = input('Database URI (bolt://) : ')
        user = input('Database user : ')
        while not user:
            user = input('Database user : ')
        password = getpass.getpass(prompt='Database password : ')
        while not password:
            password = getpass.getpass(prompt='Database password : ')
        config.read(self.conf_file)
        config['Database']['URI'] = self.uri = uri
        config['Database']['User'] = self.user = user
        config['Database']['Password'] = self.password = password
        with open(self.conf_file,  'w') as configfile:
            config.write(configfile)

    def update(self, parameter):
        config = configparser.ConfigParser()
        config.read(self.conf_file)
        write_conf = True
        if parameter == "all":
            self.create()
        elif parameter == "uri":
            uri = input('Database URI (bolt://) : ')
            while not uri:
                uri = input('Database URI (bolt://) : ')
            config['Database']['URI'] = self.uri = uri
        elif parameter == "user":
            user = input('Database user : ')
            while not user:
                user = input('Database user : ')
            config['Database']['User'] = self.user = user
        elif parameter == "password":
            password = getpass.getpass(prompt='Database password : ')
            while not password:
                password = getpass.getpass(prompt='Database password : ')
            config['Database']['Password'] = self.password = password
        else:
            print(Fore.RED, "Cannot update config ! Unvalid parameter",
                  Fore.WHITE)
            write_conf = False

        if write_conf:
            with open(self.conf_file,  'w') as configfile:
                config.write(configfile)

    def delete(self):
        config = configparser.ConfigParser()
        config.read(self.conf_file)
        config['Database'] = {'URI': 'None', 'User': 'None',
                              'Password': 'None'}
        with open(self.conf_file,  'w') as configfile:
            config.write(configfile)
        self.uri = self.user = self.password = None

    def verify(self):
        self.print()
        config = configparser.ConfigParser()
        config.read(self.conf_file)
        if config['Database']['URI'] == "None":
            return False
        if config['Database']['User'] == "None":
            return False
        if config['Database']['Password'] == "None":
            return False
        self.uri = config['Database']['URI']
        self.user = config['Database']['User']
        self.password = config['Database']['Password']
        return True
