import warnings

from neo4j import GraphDatabase
from colorama import Fore, Style


class Database:
    def __init__(self):
        self.driver = None
        warnings.filterwarnings("ignore")

    def connect(self, uri, user, password):
        try:
            self.driver = GraphDatabase.driver(uri, auth=(user, password))
            self.driver.verify_connectivity()
            print(Fore.GREEN, 'Connected to database.', Fore.WHITE)
        except Exception as e:
            print(Fore.RED, '1Error : cannot connect to db. Run "config update", "config create" or "db connect".', Fore.WHITE)
            self.driver = None

    def disconnect(self):
        if self.driver:
            self.driver.close()
            self.driver = None

    def query(self, query):
        if self.status():
            session = None
            response = None
            try:
                session = self.driver.session()
                response = session.run(query)
            except Exception as e:
                print(Fore.RED, 'Query failed : ', e, Fore.WHITE)
            return response, session

    def status(self):
        try:
            self.driver.verify_connectivity()
            return True
        except Exception as e:
            print(Fore.RED, 'Error : verify database configuration. Run "config update", "config create" or "db connect".', Fore.WHITE)
            return False
