from neo4j import GraphDatabase
from colorama import Fore, Style


class Database:
    def __init__(self):
        self.driver = None

    def connect(self, uri, user, password):
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            print(Fore.GREEN, 'Connected to database.', Fore.WHITE)
        except Exception as e:
            print(Fore.RED, 'Failed to create the driver : ', e, Fore.WHITE)

    def disconnect(self):
        if self.status():
            self.driver.close()
            self.driver = None

    def query(self, query):
        if not self.status():
            print(Fore.RED, 'Not connected to database. \
                  Need to use "db connect"!', Fore.WHITE)
        else:
            session = None
            response = None
            try:
                session = self.driver.session()
                response = session.run(query)
            except Exception as e:
                print(Fore.RED, 'Query failed : ', e, Fore.WHITE)
            return response, session

    def status(self):
        if self.driver is None:
            return False
        else:
            return True
